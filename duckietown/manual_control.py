#!/usr/bin/env python
# manual

"""
This script allows you to manually control the simulator or Duckiebot
using the keyboard arrows.
"""
from PIL import Image
import argparse
import sys
import time

import cv2
import apriltag
import gym
import numpy as np
import pyglet
from pyglet.window import key
from datetime import datetime
from time import time
from gym_duckietown.envs import DuckietownEnv

from traffic_signs import *
from tag_dict import *
from detector import *
from linalg import *
from warning_script import warning

moving_forward = True
moving = True
velocity = 0.44
previous_steps = 0
after_last_stopping = 200

# from experiments.utils import save_img

parser = argparse.ArgumentParser()
parser.add_argument("--env-name", default=None)
parser.add_argument("--map-name", default="udem1")
parser.add_argument("--distortion", default=False, action="store_true")
parser.add_argument("--camera_rand", default=False, action="store_true")
parser.add_argument("--draw-curve", action="store_true", help="draw the lane following curve")
parser.add_argument("--draw-bbox", action="store_true", help="draw collision detection bounding boxes")
parser.add_argument("--domain-rand", action="store_true", help="enable domain randomization")
parser.add_argument("--dynamics_rand", action="store_true", help="enable dynamics randomization")
parser.add_argument("--frame-skip", default=1, type=int, help="number of frames to skip")
parser.add_argument("--seed", default=1, type=int, help="seed")
args = parser.parse_args()

if args.env_name and args.env_name.find("Duckietown") != -1:
    env = DuckietownEnv(
        seed=args.seed,
        map_name=args.map_name,
        draw_curve=args.draw_curve,
        draw_bbox=args.draw_bbox,
        domain_rand=args.domain_rand,
        frame_skip=args.frame_skip,
        distortion=args.distortion,
        camera_rand=args.camera_rand,
        dynamics_rand=args.dynamics_rand,
    )
else:
    env = gym.make(args.env_name)

env.reset()
env.render()


@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
    """
    This handler processes keyboard commands that
    control the simulation
    """

    if symbol == key.BACKSPACE or symbol == key.SLASH:
        print("RESET")
        env.reset()
        env.render()
    elif symbol == key.PAGEUP:
        env.unwrapped.cam_angle[0] = 0
    elif symbol == key.ESCAPE:
        env.close()
        sys.exit(0)

    # Take a screenshot
    # UNCOMMENT IF NEEDED - Skimage dependency
    # elif symbol == key.RETURN:
    #     print('saving screenshot')
    #     img = env.render('rgb_array')
    #     save_img('screenshot.png', img)


# Register a keyboard handler
key_handler = key.KeyStateHandler()
env.unwrapped.window.push_handlers(key_handler)


def update(dt):
    global warning_text, moving_forward, velocity, previous_steps, moving, after_last_stopping
    """
    This function is called at every frame to handle
    movement/stepping and redrawing
    """
    wheel_distance = 0.102
    min_rad = 0.08

    action = np.array([0.0, 0.0])

    if moving:
        if moving_forward:
            if key_handler[key.UP]:
                action += np.array([velocity, 0.0])
            if key_handler[key.LEFT]:
                action += np.array([0, 1])
            if key_handler[key.RIGHT]:
                action -= np.array([0, 1])
        if key_handler[key.DOWN]:
            action -= np.array([velocity, 0])
    if key_handler[key.SPACE]:
        action = np.array([0, 0])

    v1 = action[0]
    v2 = action[1]
    # Limit radius of curvature
    if v1 == 0 or abs(v2 / v1) > (min_rad + wheel_distance / 2.0) / (min_rad - wheel_distance / 2.0):
        # adjust velocities evenly such that condition is fulfilled
        delta_v = (v2 - v1) / 2 - wheel_distance / (4 * min_rad) * (v1 + v2)
        v1 += delta_v
        v2 -= delta_v

    action[0] = v1
    action[1] = v2

    # Speed boost
    if key_handler[key.LSHIFT]:
        action *= 1.5
    if key_handler[key.LALT]:
        action /= 1.5


    obs, reward, done, info = env.step(action)
    # print("step_count = %s, reward=%.3f" % (env.unwrapped.step_count, reward))

    # My code start!

    step = env.step(action)
    frame = step[0]

    sign, sign_area, id = detect(frame)

    if sign != '':
        print(sign.name)

    cur_steps = step[3]['Simulator']['steps']

    after_last_stopping += 1

    if sign in influence_signs and sign_area > 500:
        if sign == Stop:
            if 2000 < sign_area < 5000:
                warning_text = 'You must stop at Stop sign!'
            if sign_area > 3500:
                if not previous_steps and after_last_stopping > 200:
                    action = np.array([0.0, 0.0])
                    moving = False
                    previous_steps = cur_steps
                elif cur_steps - previous_steps >= 40:
                    moving = True
                    previous_steps = 0
                    after_last_stopping = 0

        elif sign == DoNotEnter and sign_area > 3500:
            warning_text = 'You must stop at a no-entry sign!'
            action = np.array([0.0, 0.0])
            moving_forward = False

        elif sign == Pedestrian and sign_area > 1500 and action[0] > 0.2:
            warning_text = "You did not slow down!"
            action = np.array([0.0, 0.0])
            velocity = 0

        elif sign == Yield and sign_area > 1500 and action[0] > 0.2:
            warning_text = 'Slow down before this sign!'
            action = np.array([0.0, 0.0])
            velocity = 0

        else:
            velocity = 0.44
            moving_forward = True
            if sign.desc:
                warning_text = sign.desc
            else:
                warning_text = sign.name
    else:
        moving_forward = True
        velocity = 0.44
        warning_text = ''
    warning(warning_text)

    # My code stop!
    if key_handler[key.RETURN]:
        im = Image.fromarray(obs)
        im.save("screen.png")

    if done:
        print("done!")
        env.reset()
        env.render()

    env.render()


pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)

# Enter main event loop
pyglet.app.run()

env.close()
