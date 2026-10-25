# 把你的主页改成花叔那种效果 — 落地步骤

生成时间：2026-10-25　｜　基于 `github.com/gavenna` 的实时数据（12 个公开仓库 / 0 star / bio 为空）

## 这个目录里有什么

```
gavenna-profile/
├── README.md                                  ← 要放到 gavenna/gavenna 仓库根目录
├── assets/hero.svg                            ← 顶部横幅（矢量，可直接改文字）
├── scripts/render_stats.py                    ← 统计块渲染（已实测 5 种输入）
└── .github/workflows/update-stats.yml         ← 每小时自动刷新（已做语法校验）
```

## 一、上传（3 分钟）

我没有你的 GitHub 写权限，需要你自己执行。

**步骤 1｜建仓库**（这是关键，花叔效果的机制就在这里）

1. 打开 https://github.com/new
2. 仓库名填 **`gavenna`**（必须和用户名完全一致，差一个字符都不显示）
3. 选 **Public**，勾选 **Add a README file**
4. Create

**步骤 2｜上传这四个文件**

网页方式（最省事）：
1. 进入刚建的仓库 → 点 **Add file → Upload files**
2. 把这个目录里的 `README.md`、`assets/`、`scripts/`、`.github/` 一起拖进去
3. Commit changes

命令行方式：

```bash
git clone https://github.com/gavenna/gavenna.git
cd gavenna
# 把 gavenna-profile/ 里的东西全部复制到这里（README.md 覆盖原来的）
cp -r /d/MyselfImprove/gavenna-profile/* .
cp -r /d/MyselfImprove/gavenna-profile/.github .
git add -A && git commit -m "feat: profile README" && git push
```

**步骤 3｜验证**

- 打开 https://github.com/gavenna —— 顶部应该出现横幅 + 中文标题
- 进入仓库 → **Actions** 标签 → 左边选 `Update Stats Badges` → **Run workflow** → 等 30 秒
- 刷新主页，看统计行有没有变成 `🛠 12 个公开仓库 · 最近推送 2026-09-30`

如果 Actions 报 403：检查 workflow 里有没有 `permissions: contents: write`（已写了，不用管）。

## 二、为什么你的徽章和花叔的不一样

花叔主页是三枚徽章：`Total Stars 109.9k` / `Followers 11.9k` / `Public Repos 67`。

你现在是 **0 star / 0 follower**。把这两数字放到主页顶部，等于在门口挂一块"没什么人看"的牌子——那是负资产，不是证明。

所以脚本做了分流：**star 总数 > 0 才渲染徽章，否则渲染一行事实**。

```
stars = 0   →  🛠 12 个公开仓库 · 最近推送 2026-09-30
stars ≥ 1   →  Total Stars / Followers / Public Repos 三枚徽章
```

哪天第一个 star 出现，下一次定时任务（每小时）就自动切换。你什么都不用改。

实测记录（`python scripts/render_stats.py`）：

| 输入 | 输出 | 结果 |
|---|---|---|
| stars=0, repos=12 | 一行文字 | ✅ 幂等，无变化不写盘 |
| stars=52, followers=7 | 三枚徽章 | ✅ 链接指向正确 |
| stars=0（从徽章态回退） | 一行文字 | ✅ 可逆 |
| 标记块缺失 | 报错 exit 2 | ✅ 文件未被修改（fail-closed） |
| stars=1234, followers=11900 | `1.2k` / `11.9k` | ✅ 与花叔同格式 |

## 三、现在的真实缺口（这个比主页重要）

主页只是橱窗。我核了你 12 个仓库的实际情况，下面这些是**点了之后会掉价**的地方：

| 缺口 | 现状 | 影响 | 耗时 |
|---|---|---|---|
| **个人 bio / name / location 全空** | 右侧栏空白 | 主页最显眼的空白区 | 1 分钟 |
| **livegame 没有 README** | 点进去只看到文件列表 | 这是你最硬的作品，却最没有门面 | 30 分钟 |
| **live_tool 没有 README** | 同上 | 同上 | 20 分钟 |
| **task-priority 的 README 还是 Vite 模板** | 满屏 `@vitejs/plugin-react` 说明 | 看起来像没做完 | 15 分钟 |
| **gavenna.github.io 没有 README** | 43 MB 仓库，无说明 | 访客不知道这是什么 | 5 分钟 |
| **GVN-Blog 是空仓库** | 0 KB | 空仓库会被访客当成废弃项目 | 1 分钟（archive 或删） |

### bio 这样填（1 分钟，收益最高）

GitHub → 右上头像 → **Settings → Public profile**：

```
Name:     你的名字
Bio:      Godot + Node 做直播间互动系统 · 给 dsh 写零依赖插件
Location: 中国
Website:  https://gavenna.github.io
```

bio 会显示在主页左侧栏和每个仓库页，是**唯一会被所有访客看到的自我介绍**。

### livegame 的 README 直接复用 HANDOVER

你的 `HANDOVER.md` 里「已修复 / assumed / failed_approaches」三段结构，比 90% 的开源 README 都有说服力。把它挪到 README 里当骨架就行：

```markdown
# livegame · 抖音直播间互动游戏

弹幕/礼物 → 兵种阵营 → 战局结算 → 主播话术 → OBS 画面。
Godot 客户端 + Node 服务端 + LLM 话术引擎。

## 已经跑通的
（从 HANDOVER 的"已修复"搬过来，带根因）

## 还没验证的（诚实标注）
- LLM 话术代码完整，但 LLM_ENABLED=false，缺 API Key
- 真实弹幕/礼物链路未经实际观众验证

## 走不通的路
（从 failed_approaches 搬过来）

## 快速开始
```

**这不是包装，是把你已经在做的事说出来。** 大部分人的 README 只写"怎么用"，你的能写"哪里会坏"——这才是稀有度。

## 四、关于横幅图片

`assets/hero.svg` 是我手写的矢量图（1280×420），配色呼应你的 `dsh-aqua-glass`（深色 + 玻璃拟态光斑），已经做过 XML 合法性与元素检查（57 个节点，无 script / no foreignObject）。

**但浏览器实际渲染我没法在这里验证**——没有可用的渲染工具。如果 GitHub 上显示异常，两个降级方案：

1. 用浏览器打开 `hero.svg` → 截图存为 `assets/hero.png` → 把 README 第一行的 `hero.svg` 改成 `hero.png`
2. 想改文字：用记事本打开 `hero.svg`，搜 `把直播间做成可编程的游乐场` 直接替换（字体列表已包含 PingFang SC / Microsoft YaHei，Windows 和 Mac 都能正常显示中文）

想加邮箱的话，把 README 最后一行改成：

```markdown
[博客](https://gavenna.github.io) · 邮箱 · [全部仓库](https://github.com/gavenna?tab=repositories)
```

（我删掉了原来那个占位邮箱，不能用编的地址。）

## 五、和花叔的差距在哪（说实话）

花叔的主页之所以有效，地基是 **67 个仓库 + 109.9k star + 月均 4-6 个新品**。版式只占三成。

你的情况完全不同，但有一张牌他没打：**深度**。

| 维度 | 花叔 | 你 |
|---|---|---|
| 数量 | 67 个仓库 | 12 个 |
| 社会证明 | 109.9k star | 0 |
| 工程深度证据 | 有（工作流幂等、失败模式表） | **有，而且密度更高**（API 漂移适配表、零依赖 + I/O 注入 + vitest、HANDOVER 三分类） |
| 分发设计 | skills.json + agent 安装协议 | 无 |

所以你不该学他"多产"，该学他**把工程深度做成可被看见的形状**。他那句 "复制目录就能跑" 的对应物，在你这里是 "HANDOVER 里连走不通的路都留着"。

具体三步，按性价比排：

1. **填 bio**（1 分钟）— 让所有访客知道你做什么
2. **给 livegame 写 README**（30 分钟）— 把你最硬的东西放到能被看见的位置
3. **把 dsh-health-check 和 dsh-aqua-glass 提到主页显眼处**（已完成，在这个 README 的第二屏）

做完这三件，主页就不再是"空简历"，而是"3 个能点进去看到真东西的入口"。
