# sync_onelap_strava_agent_skills

[English](README.md)

OneLap -> Strava 同步独立 Agent Skill 发布仓库。

## 本仓库提供

- 位于 `onelap-strava-sync/` 的自包含技能包
- 位于 `onelap-strava-sync/scripts/` 的运行时 Python 代码
- 首次触发时自动创建隔离 venv 的延迟引导安装

## 快速安装

```bash
npx skills add https://github.com/yintianan/sync_onelap_strava_agent_skills
```

此命令会自动下载并在本地 OneLap Agents 环境中注册该技能。但在同步之前，您仍需运行下面的手动初始化步骤。

## 复制即用

1. 复制 `onelap-strava-sync` 到 `~/.agents/skills/`。
2. 发起 OneLap/Strava 同步请求触发技能。
3. 首次触发会创建：
   - `~/.agents/venvs/onelap-strava-sync/`
4. 依赖会从 `scripts/requirements.txt` 自动安装。

## 初始化（需手动执行）

首次使用前，请手动运行以下命令，并按命令行提示输入：

```bash
python scripts/bootstrap.py --onelap-auth-init
python scripts/bootstrap.py --strava-auth-init
```

说明：顽鹿（OneLap）密码输入为隐藏模式，命令行界面不会显示你输入的字符，这是正常现象。

**运行 `--strava-auth-init` 前**，你需要先在 Strava 网站注册自己的 API 应用，获取 `client_id` 和 `client_secret`：

1. 访问 [https://www.strava.com/settings/api](https://www.strava.com/settings/api)（需要登录）。
2. 填写应用名称等信息后提交。
3. 复制你的 `Client ID` 和 `Client Secret`，运行 `--strava-auth-init` 时按提示输入即可。

## 验收清单

- `python scripts/bootstrap.py --onelap-auth-init`
- `python scripts/bootstrap.py --strava-auth-init`
- `python scripts/bootstrap.py --since 2026-03-01`
- `python scripts/bootstrap.py --download-only --since 2026-03-01`

## 免责声明

- 本工具**仅供学习使用**。
- 请**勿**用于商业用途。
- 账户信息**仅保存于本地**。
- 请**勿**向任何 agent 输入你的账户信息。
- 使用本工具造成的后果由**用户自行承担**。

## 维护

- 运行时源码仓库：`C:/Users/13247/Documents/Code Project/opencode test`
- 同步脚本：`tools/sync_from_runtime.ps1`
