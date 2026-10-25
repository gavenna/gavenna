# 主页维护说明

部署完成：2026-10-25　｜　仓库：`gavenna/gavenna`（public，GitHub Profile README）

## 文件构成

```
gavenna-profile/
├── README.md                         主页正文（GitHub 渲染在 github.com/gavenna 顶部）
├── assets/hero.svg                   顶部横幅，1280×420 矢量图
├── scripts/render_stats.py           统计块渲染
└── .github/workflows/update-stats.yml 每小时刷新统计块
```

## 统计块怎么工作

README 里这两行是给机器人用的边界标记，**不要删**：

```markdown
<!-- STATS-START -->
🛠 13 个公开仓库 · 最近推送 2026-10-25
<!-- STATS-END -->
```

`update-stats.yml` 每小时第 17 分跑一次：

1. GraphQL 抓全量 star / follower / 仓库数 / 最近推送日期（超过 100 个仓库自动翻页）
2. 调 `scripts/render_stats.py` 重写标记块之间的内容
3. 无变化就不提交

**分流规则**：`stars = 0` 时渲染一行文字（0 值徽章是负资产），`stars ≥ 1` 时自动切换成三枚徽章。第一个 star 出现的下一个整点就会跳变，不需要手动改。

手动触发：仓库 → Actions → `Update Stats Badges` → Run workflow。

## 改横幅文字

用记事本打开 `assets/hero.svg`，搜 `把直播间做成可编程的游乐场` 直接替换。字体列表已含 PingFang SC / Microsoft YaHei，Windows 和 Mac 都能正常显示中文。

如果 GitHub 上显示异常：浏览器打开 `hero.svg` 截图存为 `hero.png`，把 README 第一行的 `hero.svg` 改成 `hero.png`。

## 待办

- [ ] **填 bio 和 Website** → https://github.com/settings/profile
      Bio 建议：`Godot + Node 做直播间互动系统`
      Website：`https://gavenna.github.io`
- [ ] **清掉 GitHub status**（当前显示「On vacation」，会占住主页描述位）
- [ ] **给 livegame 写 README** —— `HANDOVER.md` 的「已修复 / assumed / failed_approaches」三分类挪上去就是现成的骨架，比大多数开源 README 有说服力
- [ ] **给 live_tool 写 README**
- [ ] **`task-priority` 的 README 还是 Vite 默认模板**，换掉或补一段
- [ ] **`GVN-Blog` 是空仓库**，archive 或删除

## 维护提醒

- 每小时的定时任务只能验证"能跑"，验证不了"跑对了"。偶尔去 Actions 看一眼日志里的 `stars=... repos=... latest=...` 是否和主页数字一致。
- workflow 的 token 权限需要 `contents: write`（已写在文件里），改 workflow 时别删。
