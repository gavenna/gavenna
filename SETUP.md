# 主页维护说明

仓库：`gavenna/gavenna`（public，GitHub Profile README）　｜　最后更新：2026-10-25

## 设计原则

主页只展示 **livegame** 一个项目。其它仓库即使 public 也不在主页露出——主页是作品集，不是仓库清单。

## 文件构成

```
gavenna-profile/
├── README.md          主页正文（渲染在 github.com/gavenna 顶部）
├── assets/hero.svg    顶部横幅，1280×420 矢量图
└── SETUP.md           本文件
```

## 改横幅文字

用记事本打开 `assets/hero.svg`，直接搜要改的字替换。字体列表已含 PingFang SC / Microsoft YaHei，Windows 和 Mac 都能正常显示中文。

底部五枚标签（Godot / Node / 弹幕链路 / LLM 话术 / 一键启动）每个是一组 `<rect>` + `<text>`。改文字时若字数变化明显，要同步调 `<rect>` 的 `width` 和 `<text>` 的 `x`（`x` = rect 的 `x` + `width` / 2），否则胶囊里会偏。

如果 GitHub 上显示异常：浏览器打开 `hero.svg` 截图存为 `hero.png`，把 README 第一行的 `hero.svg` 改成 `hero.png`。

## 已移除：自动统计块

原来 README 里有一块每小时自动更新的统计（公开仓库数 / 最近推送），靠 `.github/workflows/update-stats.yml` 驱动。
2026-10-25 随「主页只保留 livegame」一起删了——那行数字展示的是仓库总数，与聚焦单一项目的定位冲突。

要恢复的话，需要重新加回 workflow、`scripts/render_stats.py`、以及 README 里的
`<!-- STATS-START -->` / `<!-- STATS-END -->` 标记对。当年踩过的两个坑记在这里以免重踩：

- GraphQL 查询必须带 `privacy: PUBLIC`，否则用个人 PAT 跑会把自己的私有仓库算进「公开仓库」数
- `LATEST` 要先 `select(. != null)` 再取 `max`，空仓库列表时 jq 会直接报错并输出 `"null"` 字面量

## 待办

- [ ] **填 bio 和 Website** → https://github.com/settings/profile
      Bio 建议：`Godot + Node 做直播间互动系统`　Website：`https://gavenna.github.io`
- [ ] **清掉 GitHub status**（当前显示「On vacation」，会占住主页描述位）
- [ ] **给 livegame 写 README** —— `HANDOVER.md` 的「已修复 / assumed / failed_approaches」三分类挪上去就是现成骨架
- [ ] 其余不展示的仓库：主页已不再链接它们，但它们仍是 public，GitHub 仓库页可见。要彻底不露出需逐个设为 private 或 archive
