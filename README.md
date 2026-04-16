# remove-bg

本地去背工具，基於 [rembg](https://github.com/danielgatis/rembg)（U2Net 模型），完全離線、免費。

## 使用方式

1. 將圖片放入 `source/` 資料夾
2. 執行腳本：

```bash
./run.sh
```

3. 去背結果會輸出至 `output/`，檔名與原檔相同（副檔名統一為 `.png`）

## 支援格式

| 輸入 | 輸出 |
|------|------|
| .png / .jpg / .jpeg / .webp | .png（透明背景） |

## 環境需求

- Python 3.7+
- 首次執行時 `run.sh` 會自動安裝所需套件

## 手動安裝套件

```bash
pip3 install -r requirements.txt
```
