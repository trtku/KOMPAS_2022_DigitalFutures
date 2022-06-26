# Digital Futures 2022 WS

> Programmings for digital fabrication in architecture with compas

This is a hands-on style workshop to introduce basics of COMPAS, a python framework developed at ETH Zurich aiming to construct continuous workflow from computatoinal design to robotic fabrication. Depending on the procedure of WS, the host will introduce fundamentals of COMPAS FAB: a robotic fabrication package providing interface to ROS. This allows us to simulate robotic motions in Rhinoceros and Grasshopper without actual robot. At the end of this workshop, participants will learn the principle of COMPAS and its application to robotic fabrication.
スイス連邦工科大を中心に開発中のパイソンフレームワーク、”COMPAS”の入門ワークショップ。”COMPAS”の基礎から始まり、進捗に応じて拡張機能の一つ、”COMPAS FAB”の紹介も予定。RhinocerosやGrasshopper上でロボットアームのシミュレーションが可能になります。急速な広がりを見せる”COMPAS”をベースに、コンピューテーショナルデザインからロボッティクファブリケーションまでをカバーする入門ワークショップ。

## Schedule / スケジュール

| Lecture　レクチャー | Date　日付   | Session content　セッション内容                                                                                                                                                                                                                                                                                                                                                                                                                          | Session leads　担当      |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 01      | 28.06. | **Introduction and COMPAS / イントロダクション・CONPASの紹介**<br>Introduction to the course and COMPAS / COMPAS入門<br>👉[Go to lecture　レクチャーページへ](lecture_01/README.md)                                                                                                                                                               | Ko　鶴田                |
| 02      | 29.06. | **COMPAS FAB / COMPAS FABの紹介**<br>Introduction to COMPAS FAB and excercises. (from robotic fundamentals to path planning) / COMPAS　FAB入門及びエクササイズ（ロボットの基礎からパスプランニングまで）<br>👉[Go to lecture　レクチャーページへ](lecture_02/README.md)                                                                                                                                                                                                           | Ko　鶴田       |
| 03      | 30.06. | **Continuation and Recap / エクササイズ・リキャップ**<br>Continuation of excercises with on-demad help. Final review and recap.<br>👉[Go to lecture　レクチャーページへ](lecture_03/README.md)                                                                                                                                                                                        | Ko　鶴田       |


## Information　インフォメーション

Links　リンク:
[DigitalFutures2022 Workshops](https://digitalfutures.international/workshop/programmings-for-digital-fabrication-in-architecture-with-compas/) |
[Slack workspace](https://join.slack.com/t/digitalfuture2022ws/shared_invite/zt-1brmimbtc-XRDzAF36pFCYHiYqCLywKQ) |
[COMPAS docs](https://compas.dev) |
[COMPAS FAB docs](https://gramaziokohler.github.io/compas_fab/latest/)

### Objectives　目的

1. Understand fundamentals of robotics, coordinate systems, and transformations. / ロボティクスの基礎、座標系、トランスフォーメーション、などの基礎的な理解
1. Apply these concepts to design and implement digital fabrication processes. / 上記の概念の、デジタルファブリケーションのデザイン及び実践への応用
1. Gain an understanding of different robot control methods and their application. / 異なるロボットコントロールの方法とその応用の理解
1. See potentials to bring the knowledge you have learn here to your practice. / 本WSで得られる知識を各参加者の実践へとつなげていく可能性を考える


### Content　コンテンツ

Lectures, tutorials and exercises will focus on / WSでは以下の内容に焦点をあてる予定です:

* Introduction to fundamentals of robotics. / ロボット基礎への導入
* Introduction to COMPAS framework and core extensions for digital fabrication (fab) / COMPASと拡張ライブラリへの導入
* Integration of planning tools into parametric design environment (CAD). / CADソフトウェアへの統合
* Overview and usage of ROS (Robot Operating System). / ROSの概観
* Design of digital fabrication processes(simulation). / デジタルファブリケーションデザインの実践（シミュレーション）

## Requirements　必須ソフトウェア

* Minimum OS / ミニマムOS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer. / インスタレーション後に、使用コンピュータのBIOSでのVirtualizationをEnableする必要があります。

## Installation / インストール手順

We use `conda` to make sure we have clean, isolated environment for dependencies.
独立した簡潔な環境を構築するため、`conda`を使用します。

<details><summary>First time using <code>conda</code>? / 初めて<code>conda</code>を使用する場合</summary>
<p>

Make sure you run this at least once:
少なくとも一度は以下のコマンドを走らせてください：

    (base) conda config --add channels conda-forge

![image of anaconda](https://github.com/trtku/KOMPAS_2022_DigitalFutures/blob/main/img/conda%201%20add%20conda%20forge.PNG)

</p>
</details>

1. Create a environment with compas and compas_fab / 必要なライブラリとともに環境を構築する

    (base) conda create -n df2022 -c conda-forge compas compas_fab

![image of anaconda](https://github.com/trtku/KOMPAS_2022_DigitalFutures/blob/main/img/conda%201%20add%20conda%20forge.PNG)


1.  Add to Rhino / ライノセラスにコンパスをインストールする

    (base)   conda activate df2022
    (df2022) python -m compas_rhino.install -v 7.0

1.  Get the workshop files / 本ワークショップ用のファイルをクローンする

    (df2022) cd PATH_TO_YOUR_WORKING_DIRECTORY
    (df2022) git clone https://github.com/trtku/KOMPAS_2022_DigitalFutures.git

1.  Verify installation / インスタレーションの確認

    (df2022) python -m compas
    (df2022) python -m compas_fab

1.  Open Visual Studio Code / Visual Studio Code を開く

    (df2022) code .

（Open Rhinoceros3D and Grasshopper if necessary. / 必要に応じてライノセラス、グラスホッパーを開く）

🚀 You're ready! / 準備完了です！

## Credits / クレジット

This repository is arranged for DigitalFUTURES 2022 workshop based on a COMPAS course at ETH Zurich. ([see original repo](https://github.com/compas-teaching/COMPAS-II-FS2022))

Arranged by Ko Tsuruta (<trtku0809@gmail.com>); with the help of Gonzalo Casas (<casas@arch.ethz.ch>).

本レポジトリはスイス連邦工科大で行われているCOMPASコースをもとにDigitalFUTURES2022ワークショップ用にアレンジをしたものです。

アレンジはGonzalo　Casasサポートのもと、鶴田航が行いました。
