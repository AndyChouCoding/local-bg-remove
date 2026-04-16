# remove-bg

A local background removal tool powered by [rembg](https://github.com/danielgatis/rembg) (U2Net model). Fully offline and free.

## Usage

1. Drop your images into the `source/` folder
2. Double-click `run.command` to run
3. Results are saved to `output/` with the original filename (`.png`)

## Supported Formats

| Input | Output |
|-------|--------|
| .png / .jpg / .jpeg / .webp | .png (transparent background) |

## Requirements

- Python 3.7+
- Dependencies are installed automatically on first run

## Manual Install

```bash
pip3 install -r requirements.txt
```

> **Note:** If macOS shows "cannot be opened because the developer cannot be verified", go to **System Settings → Privacy & Security** and click "Open Anyway".

---

# remove-bg（中文說明）

本地去背工具，基於 [rembg](https://github.com/danielgatis/rembg)（U2Net 模型），完全離線、免費。

## 使用方式

1. 將圖片放入 `source/` 資料夾
2. 雙擊 `run.command` 執行
3. 去背結果輸出至 `output/`，保留原始檔名（副檔名統一為 `.png`）

## 支援格式

| 輸入 | 輸出 |
|------|------|
| .png / .jpg / .jpeg / .webp | .png（透明背景） |

## 環境需求

- Python 3.7+
- 首次執行時自動安裝所需套件

## 手動安裝套件

```bash
pip3 install -r requirements.txt
```

> **注意：** 若 macOS 顯示「無法開啟，因為無法驗證開發者」，至 **系統設定 → 隱私權與安全性** 點選「仍要開啟」即可。
