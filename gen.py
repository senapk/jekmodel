#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import io
import shutil

BASE = "base"
TARGET = "_posts"
REMOTE = 'https://raw.githubusercontent.com/senapk/jekmodel/master/base'

shutil.rmtree(TARGET)
os.mkdir(TARGET)
hooks = os.listdir(BASE)
for hook in hooks:
    lines = []
    with open(BASE + os.sep + hook + os.sep + "Readme.md") as f:
        lines = f.readlines()
    title = lines[0][:-1] #remove \n
    words = title.split(" ")[1:] #remove ##
    date = [x for x in words if x.startswith("$")]
    words = [x for x in words if not x in date]
    tags = [x for x in words if x.startswith("#")]
    words = [x for x in words if not x in tags]

    title = ' '.join(words)
    tags = [x[1:] for x in tags] #removing #
    if len(date) > 0:
        date = date[0][1:] #removing $
    else:
        date = None

    out = io.StringIO()
    out.write("---\nlayout: post\n")
    out.write("title: " + title + '\n')
    out.write("image: " + REMOTE + "/" + hook + "/__capa.jpg\n")
    out.write("tags:\n")
    for t in tags:
        out.write("- " + t + "\n")
    out.write("---\n")
    out.write("".join(lines[1:]))
    text = out.getvalue()
    text = text.replace("[](__capa.jpg)", "")
    with open(TARGET + os.sep + date + "-" + title + ".md", "w") as f:
        f.write(text)

"""
---
layout: post
title: "Seja bem-vindo"
description: Lorem ipsum dolor sit amet, consectetur adipisicing elit.
image: 'http://res.cloudinary.com/dm7h7e8xj/image/upload/c_scale,w_760/v1504807239/morpheus_xdzgg1.jpg'
category: 'blog'
twitter_text: Lorem ipsum dolor sit amet, consectetur adipisicing elit.
introduction: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
---
tags:
- vuejs
- javascript
- tutorial
    
"""

    