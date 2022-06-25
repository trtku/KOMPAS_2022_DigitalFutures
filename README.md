# Digital Futures 2022 WS

> Programmings for digital fabrication in architecture with compas

This is a hands-on style workshop to introduce basics of COMPAS, a python framework developed at ETH Zurich aiming to construct continuous workflow from computatoinal design to robotic fabrication. Depending on the procedure of WS, the host will introduce fundamentals of COMPAS FAB: a robotic fabrication package providing interface to ROS. This allows us to simulate robotic motions in Rhinoceros and Grasshopper without actual robot. At the end of this workshop, participants will learn the principle of COMPAS and its application to robotic fabrication. スイス連邦工科大を中心に開発中のパイソンフレームワーク、”COMPAS”の入門ワークショップ。”COMPAS”の基礎から始まり、進捗に応じて拡張機能の一つ、”COMPAS FAB”の紹介も予定。RhinocerosやGrasshopper上でロボットアームのシミュレーションが可能になります。急速な広がりを見せる”COMPAS”をベースに、コンピューテーショナルデザインからロボッティクファブリケーションまでをカバーする入門ワークショップ。

## Schedule, DF 2022

| Lecture | Date   | Session content                                                                                                                                                                                                                                                                                                                                                                                                                          | Session leads      |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 01      | 28.06. | **Introduction**<br>Introduction to digital fabrication methods and the COMPAS ecosystem for digital fabrication: core, fab, rrc, slicer.<br>Brief overview of core data structures (network, mesh).<br>Remote procedure calls.<br>👉[Go to lecture](lecture_01/README.md)                                                                                                                                                               | All                |
| 02      | 29.06. | **Robotic fundamentals**<br>Introduction to robotics: anatomy of an industrial robot, coordinate systems, transformations.<br>Brief intro to kinematic functions and path planning.<br>👉[Go to lecture](lecture_02/README.md)                                                                                                                                                                                                           | GKR (RR, GC)       |
| 03      | 30.06. | **Robot models**<br>Models from URDF, programmatic models.<br>Robot model visualization in Rhino / Grasshopper.<br>Forward kinematics of open chain manipulators.<br>Assignment: model your own robot.<br>👉[Go to lecture](lecture_03/README.md)                                                                                                                                                                                        | GKR (RR, GC)       |


## Information

Links:
[DigitalFutures2022 Workshops](https://digitalfutures.international/workshop/programmings-for-digital-fabrication-in-architecture-with-compas/) |
[Slack workspace](https://join.slack.com/t/digitalfuture2022ws/shared_invite/zt-1brmimbtc-XRDzAF36pFCYHiYqCLywKQ) |
[COMPAS docs](https://compas.dev)
[COMPAS FAB docs](https://gramaziokohler.github.io/compas_fab/latest/)

### Objectives

1. Understand fundamentals of robotics, coordinate systems, transformations and orientation representations.
1. Apply these concepts to design and implement digital fabrication processes.
1. Gain an understanding of different robot control methods and their application.
1. See potentials to bring the knowledge you have learn here to your practice.


### Content

Lectures, tutorials and exercises will focus on:

* Introduction to fundamentals of robotics.
* Introduction to COMPAS framework and core extensions for digital fabrication (fab)
* Robot model representations.
* Robot forward and inverse kinematics.
* Robot path planning: Cartesian motion planning and kinematic motion planning, planning scene and collision detection.
* Integration of planning tools into parametric design environment (CAD).
* Overview and usage of ROS (Robot Operating System).
* Design of digital fabrication processes (assembly of discrete elements, 3D printing, etc.).

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>

    (base) conda env create -f https://dfab.link/fs2022.yml

### Add to Rhino

    (base)   conda activate fs2022
    (fs2022) python -m compas_rhino.install -v 7.0

### Get the workshop files

    (fs2022) cd Documents
    (fs2022) git clone https://github.com/compas-teaching/COMPAS-II-FS2022

### Verify installation

    (fs2022) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.14.1
    Python: 3.8.10 | packaged by conda-forge | (default, May 11 2021, 06:25:23) [MSC v.1916 64 bit (AMD64)]
    Extensions: ['compas-fab', 'compas-cgal', 'compas-rrc', 'compas-slicer']

### Update installation

To update your environment:

    (fs2022) conda env update -f https://dfab.link/fs2022.yml
