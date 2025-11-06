# 設計書

## プロジェクト概要

**複数占い手法統合システム（Multi-Method Fortune Telling System）**

データベース駆動型のアーキテクチャで、5つ以上の占い手法を統合し、多角的な運勢分析を提供する占いアプリケーション。

---

## 1. 技術スタック

### バックエンド
- **言語**: Python 3.x
- **Webフレームワーク**: Flask
- **テンプレートエンジン**: Jinja2
- **データベース**: SQLite
- **ORM**: SQLAlchemy（推奨）

### フロントエンド
- **UI**: シンプルなHTML/CSS + JavaScript
- **視覚化**: HTML/CSS プログレスバー、カラーコーディング
- **将来的な拡張**: Chart.js（レーダーチャート）

### 占い計算ライブラリ
- **西洋占星術**: pyswisseph（Swiss Ephemeris）
- **その他**: 標準ライブラリ + カスタム実装

### 将来的な拡張
- **LLM統合**: Claude API または OpenAI API（総合判断の自然文生成）

---

## 2. MVPスコープ（Phase分け）

### Phase 1（最小MVP） - 初期実装
- ✅ ユーザー情報入力（生年月日のみ）
- ✅ 5つの占い手法による分析
  - 西洋占星術
  - タロット占い
  - 数秘術
  - 四柱推命
  - 易経
- ✅ 個別結果と総合判断の表示（シンプル版）
- ✅ 運勢カテゴリー別分析（恋愛・仕事・健康・金運）
- ✅ シンプルなHTML/CSS視覚化（プログレスバー）

### Phase 2（機能拡張）
- 履歴管理（保存・閲覧機能）
- 視覚化の強化（チャート・グラフ）
- 根拠の透明性（計算ロジック説明）
- 出生時刻・出生地の対応

### Phase 3（管理機能）
- 管理画面（占い手法のデータベース管理）
- 新規手法の追加・更新・無効化機能

---

## 3. 占い手法の実装レベル

### 方針
**オプションB（中程度版）+ 伝統的な占術理論に忠実**

### 各手法の実装詳細

#### 3.1 西洋占星術
- 主要天体の位置計算（太陽、月、水星、金星、火星、木星、土星）
- 12ハウスシステム（Placidusハウス）
- 主要アスペクト（合、セクスタイル、スクエア、トライン、オポジション）
- **使用ライブラリ**: pyswisseph
- **計算基準**: 生年月日から出生図（ネイタルチャート）の簡易版を作成

#### 3.2 タロット占い
- **カード構成**: 大アルカナ22枚 + 小アルカナ56枚（計78枚）
- **スプレッド**: 3枚引き（過去・現在・未来）
- **解釈**: 正位置・逆位置の両対応
- **カテゴリー別意味**: 恋愛・仕事・健康・金運ごとに異なる解釈
- **データ管理**: データベースに全カードの意味を格納

#### 3.3 数秘術
- **ライフパスナンバー**（誕生数）: 生年月日の数字を還元
- **パーソナルイヤーナンバー**: 現在の年運
- **マスターナンバー**: 11, 22, 33の特別扱い
- **計算ロジック**: 各桁の和を1桁になるまで還元（マスターナンバー除く）

#### 3.4 四柱推命
- **四柱計算**: 年柱・月柱・日柱・時柱の天干地支
- **十干十二支**: 正確な暦計算
- **通変星**: 比肩、劫財、食神、傷官、偏財、正財、偏官、正官、偏印、印綬
- **五行バランス**: 木火土金水の分析
- **相性関係**: 刑冲破害合の分析
- **データ管理**: 十干・十二支・通変星のマスターデータをデータベースに格納

#### 3.5 易経
- **卦の体系**: 64卦
- **卦の生成**: 筮竹法のシミュレート（確率分布は正確に）
- **解釈**: 本卦と之卦（変爻がある場合）
- **カテゴリー別意味**: 各卦の恋愛・仕事・健康・金運の解釈
- **データ管理**: 64卦と8つの基本卦（八卦）をデータベースに格納

---

## 4. 総合判断のアルゴリズム

### 方針
**カテゴリー別スコアリング + 重み付け平均**

### アルゴリズム詳細

#### 4.1 個別手法のスコアリング
各占い手法が運勢カテゴリーごとにスコアを算出：
- **範囲**: 0〜100点
- **カテゴリー**: 恋愛運、仕事運、健康運、金運

#### 4.2 総合スコア計算
```python
総合スコア = Σ(各手法のスコア) / 手法数
```

例（恋愛運）:
- 西洋占星術: 85点
- タロット: 60点
- 数秘術: 75点
- 四柱推命: 70点
- 易経: 80点
- **平均**: 74点

#### 4.3 評価レベル変換
スコアから評価テキストへの変換：
- 90-100点: "非常に良好"
- 75-89点: "良好"
- 60-74点: "普通"
- 40-59点: "やや注意"
- 0-39点: "注意が必要"

#### 4.4 将来的な拡張（Phase 2以降）
- **LLM統合**: Claude APIやOpenAIを使用し、各手法の結果を踏まえた自然な解釈文を生成
- **矛盾の処理**: 手法間で大きく異なる結果が出た場合の調整ロジック
- **重み付け**: 手法ごとに得意分野に応じた重み付け

---

## 5. ユーザー認証

### 方針
**認証なし**

### 理由
- ローカル環境での個人使用を想定
- シンプルさを優先
- セットアップの簡易化

### 将来的な拡張（Phase 2以降）
- 簡易ユーザー管理（名前のみ）を追加し、履歴を個人別に管理する選択肢

---

## 6. データベーススキーマ設計

### 6.1 命名規則

#### テーブル名
```
{手法名}_{データ種別}

例:
- tarot_cards
- shichu_stems
- iching_hexagrams
- fortune_methods（共通）
- analysis_results（共通）
```

#### カラム名
```
- 日本語名: name_ja
- 英語名: name_en
- 中国語名: name_zh
- 運勢カテゴリー別: {category}_meaning または {category}_trait
  例: love_meaning, work_trait
- スコア: {category}_score
- フラグ: is_{状態}
  例: is_active, is_reversed
- 日時: {action}_at
  例: created_at, updated_at
```

### 6.2 テーブル定義

#### 共通テーブル

##### fortune_methods（占い手法マスター）
```sql
CREATE TABLE fortune_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
    category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

##### analysis_results（占い結果保存 - Phase 2用）
```sql
CREATE TABLE analysis_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    birth_date DATE NOT NULL,
    birth_time TIME,
    birth_place TEXT,
    analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    results_json TEXT,
    overall_score_love INTEGER,
    overall_score_work INTEGER,
    overall_score_health INTEGER,
    overall_score_money INTEGER
);
```

#### 西洋占星術テーブル

##### zodiac_signs（12星座）
```sql
CREATE TABLE zodiac_signs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    symbol TEXT,
    element TEXT,                    -- "火", "地", "風", "水"
    quality TEXT,                    -- "活動宮", "不動宮", "柔軟宮"
    ruling_planet TEXT,              -- 支配星
    date_range_start TEXT,           -- "03-21"
    date_range_end TEXT,             -- "04-19"
    love_trait TEXT,
    work_trait TEXT,
    health_trait TEXT,
    money_trait TEXT
);
```

##### astrology_planets（天体）
```sql
CREATE TABLE astrology_planets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    symbol TEXT,
    ruling_sign TEXT,                -- 支配する星座
    meaning TEXT,                    -- 天体の意味
    love_influence TEXT,
    work_influence TEXT,
    health_influence TEXT,
    money_influence TEXT
);
```

##### astrology_houses（ハウス）
```sql
CREATE TABLE astrology_houses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house_number INTEGER NOT NULL,   -- 1-12
    name_ja TEXT NOT NULL,
    meaning TEXT,
    life_area TEXT                   -- 担当する人生領域
);
```

##### astrology_aspects（アスペクト）
```sql
CREATE TABLE astrology_aspects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    angle REAL NOT NULL,             -- 0, 60, 90, 120, 180
    orb REAL,                        -- 許容誤差
    aspect_type TEXT,                -- "major" or "minor"
    is_harmonious BOOLEAN,           -- 調和的か否か
    meaning TEXT
);
```

#### タロットテーブル

##### tarot_cards（タロットカード）
```sql
CREATE TABLE tarot_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number INTEGER NOT NULL,    -- 0-77
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    arcana_type TEXT NOT NULL,       -- "major" or "minor"
    suit TEXT,                       -- "wands", "cups", "swords", "pentacles"（小アルカナのみ）
    rank TEXT,                       -- "ace", "2"-"10", "page", "knight", "queen", "king"
    upright_general TEXT,
    upright_love TEXT,
    upright_work TEXT,
    upright_health TEXT,
    upright_money TEXT,
    reversed_general TEXT,
    reversed_love TEXT,
    reversed_work TEXT,
    reversed_health TEXT,
    reversed_money TEXT,
    keywords TEXT                    -- キーワード（カンマ区切り）
);
```

#### 数秘術テーブル

##### numerology_meanings（数秘術の数字解釈）
```sql
CREATE TABLE numerology_meanings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL UNIQUE,  -- 1-9, 11, 22, 33
    is_master_number BOOLEAN DEFAULT 0,
    general_meaning TEXT,
    personality_trait TEXT,
    love_meaning TEXT,
    work_meaning TEXT,
    health_meaning TEXT,
    money_meaning TEXT,
    strengths TEXT,
    weaknesses TEXT
);
```

#### 四柱推命テーブル

##### shichu_stems（十干）
```sql
CREATE TABLE shichu_stems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stem_name_ja TEXT NOT NULL,      -- "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"
    stem_name_zh TEXT,
    stem_name_en TEXT,               -- "Kou", "Otsu", etc.
    element TEXT NOT NULL,           -- "木", "火", "土", "金", "水"
    polarity TEXT NOT NULL,          -- "陽", "陰"
    order_num INTEGER NOT NULL,      -- 1-10
    general_meaning TEXT,
    personality_trait TEXT
);
```

##### shichu_branches（十二支）
```sql
CREATE TABLE shichu_branches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_name_ja TEXT NOT NULL,    -- "子", "丑", "寅"...
    branch_name_zh TEXT,
    branch_name_en TEXT,
    zodiac_animal TEXT,              -- "鼠", "牛", "虎"...
    element TEXT NOT NULL,           -- "水", "土", "木"...
    order_num INTEGER NOT NULL,      -- 1-12
    month_association INTEGER,       -- 対応する月（1-12）
    general_meaning TEXT,
    personality_trait TEXT
);
```

##### shichu_hidden_stems（蔵干）
```sql
CREATE TABLE shichu_hidden_stems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_id INTEGER NOT NULL,
    hidden_stem_id INTEGER NOT NULL,
    stem_type TEXT,                  -- "本気", "中気", "余気"
    strength INTEGER,                -- 1-3（1が弱、3が強）
    FOREIGN KEY (branch_id) REFERENCES shichu_branches(id),
    FOREIGN KEY (hidden_stem_id) REFERENCES shichu_stems(id)
);
```

##### shichu_tonhensei（通変星）
```sql
CREATE TABLE shichu_tonhensei (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,           -- "比肩", "劫財", "食神", "傷官", "偏財", "正財", "偏官", "正官", "偏印", "印綬"
    name_zh TEXT,
    category TEXT,                   -- "比肩", "洩星", "財星", "官星", "印星"
    general_meaning TEXT,
    personality_trait TEXT,
    love_meaning TEXT,
    work_meaning TEXT,
    health_meaning TEXT,
    money_meaning TEXT,
    strengths TEXT,
    weaknesses TEXT
);
```

##### shichu_combinations（干支の相性・刑冲破害）
```sql
CREATE TABLE shichu_combinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    combination_type TEXT NOT NULL,  -- "合", "冲", "刑", "破", "害", "三合", "方合"
    element1_type TEXT NOT NULL,     -- "stem" or "branch"
    element1_id INTEGER NOT NULL,
    element2_type TEXT NOT NULL,
    element2_id INTEGER NOT NULL,
    element3_id INTEGER,             -- 三合などの場合
    result_element TEXT,             -- 合化した場合の五行
    effect_description TEXT,
    is_positive BOOLEAN,
    impact_love INTEGER,             -- -100 to 100
    impact_work INTEGER,
    impact_health INTEGER,
    impact_money INTEGER
);
```

#### 易経テーブル

##### iching_trigrams（八卦）
```sql
CREATE TABLE iching_trigrams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trigram_number INTEGER NOT NULL, -- 1-8
    name_ja TEXT NOT NULL,           -- "乾", "兌", "離", "震", "巽", "坎", "艮", "坤"
    name_zh TEXT,
    name_en TEXT,
    symbol TEXT,                     -- "☰", "☱", etc.
    binary_code TEXT,                -- "111", "011", etc.
    element TEXT,                    -- 対応する五行
    nature TEXT,                     -- "天", "沢", "火", "雷", "風", "水", "山", "地"
    attribute TEXT,                  -- 属性
    meaning TEXT
);
```

##### iching_hexagrams（64卦）
```sql
CREATE TABLE iching_hexagrams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hexagram_number INTEGER NOT NULL UNIQUE, -- 1-64
    name_ja TEXT NOT NULL,
    name_zh TEXT,
    name_en TEXT,
    symbol TEXT,                     -- "䷀" etc.
    trigram_upper_id INTEGER,        -- 上卦（八卦テーブルへの参照）
    trigram_lower_id INTEGER,        -- 下卦
    binary_code TEXT,                -- "111111" etc.
    general_meaning TEXT,
    judgment_text TEXT,              -- 卦辞
    image_text TEXT,                 -- 象伝
    love_meaning TEXT,
    work_meaning TEXT,
    health_meaning TEXT,
    money_meaning TEXT,
    advice TEXT,
    FOREIGN KEY (trigram_upper_id) REFERENCES iching_trigrams(id),
    FOREIGN KEY (trigram_lower_id) REFERENCES iching_trigrams(id)
);
```

##### iching_lines（爻辞）
```sql
CREATE TABLE iching_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hexagram_id INTEGER NOT NULL,
    line_position INTEGER NOT NULL,  -- 1-6（初爻から上爻）
    line_type TEXT,                  -- "陰" or "陽"
    line_text TEXT,                  -- 爻辞
    meaning TEXT,
    FOREIGN KEY (hexagram_id) REFERENCES iching_hexagrams(id)
);
```

---

## 7. 視覚化方法

### Phase 1の実装
**オプションB: シンプルなHTML/CSS**

#### 実装内容
- **プログレスバー**: 各運勢カテゴリーのスコアを視覚化
- **カラーコーディング**: スコアに応じた色分け
  - 90-100点: 緑（#4CAF50）
  - 75-89点: 黄緑（#8BC34A）
  - 60-74点: 黄色（#FFC107）
  - 40-59点: オレンジ（#FF9800）
  - 0-39点: 赤（#F44336）
- **星評価**: ★★★★☆ のような視覚的表現
- **レスポンシブデザイン**: モバイルでも見やすい

#### HTML/CSS例
```html
<div class="fortune-category">
    <h3>恋愛運</h3>
    <div class="progress-bar">
        <div class="progress-fill" style="width: 74%; background-color: #FFC107;"></div>
    </div>
    <p class="score">74点 / 普通</p>
    <p class="stars">★★★★☆</p>
</div>
```

### Phase 2以降の拡張
- **Chart.js**: レーダーチャート（4つの運勢カテゴリーを一度に表示）
- **グラフ比較**: 各占い手法のスコアを並べて比較
- **時系列グラフ**: 過去の占い結果との比較

---

## 8. プロジェクト構造

```
fortune-telling/
├── app/
│   ├── __init__.py
│   ├── models.py              # SQLAlchemyモデル
│   ├── database.py            # DB接続・初期化
│   ├── routes.py              # Flaskルート定義
│   ├── fortune/
│   │   ├── __init__.py
│   │   ├── astrology.py       # 西洋占星術ロジック
│   │   ├── tarot.py           # タロットロジック
│   │   ├── numerology.py      # 数秘術ロジック
│   │   ├── shichu.py          # 四柱推命ロジック
│   │   └── iching.py          # 易経ロジック
│   ├── analyzer.py            # 総合分析エンジン
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html         # 入力フォーム
│   │   └── result.html        # 結果表示
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── data/
│   ├── fortune.db             # SQLiteデータベース
│   └── seed_data/             # 初期データ投入用
│       ├── tarot_data.json
│       ├── shichu_data.json
│       └── iching_data.json
├── tests/
│   ├── test_astrology.py
│   ├── test_tarot.py
│   └── ...
├── .kiro/
│   └── specs/
│       └── multi-method-fortune-telling/
│           ├── requirements.md  # 要件定義書
│           └── design.md        # 本設計書
├── requirements.txt
├── config.py
└── run.py                     # アプリケーション起動
```

---

## 9. 開発の流れ

### Phase 1実装ステップ

1. **環境セットアップ**
   - Python仮想環境作成
   - 必要なライブラリインストール（Flask, SQLAlchemy, pyswisseph等）

2. **データベース構築**
   - SQLiteデータベース作成
   - テーブル定義実行
   - 初期データ投入（マスターデータ）

3. **各占い手法の実装**
   - 西洋占星術モジュール
   - タロットモジュール
   - 数秘術モジュール
   - 四柱推命モジュール
   - 易経モジュール

4. **総合分析エンジンの実装**
   - スコアリングロジック
   - 統合アルゴリズム

5. **Webアプリケーション実装**
   - Flaskルート
   - 入力フォーム（生年月日）
   - 結果表示画面

6. **視覚化の実装**
   - CSS スタイリング
   - プログレスバー、カラーコーディング

7. **テスト**
   - 単体テスト
   - 統合テスト
   - 実際のデータでの動作確認

---

## 10. 技術的課題と解決策

### 課題1: 西洋占星術の天体計算の複雑さ
**解決策**: pyswissephライブラリの使用により、正確な天体位置計算を実現

### 課題2: タロットの解釈の多様性
**解決策**: データベースに複数の解釈パターンを格納し、カテゴリー別に適切な解釈を選択

### 課題3: 四柱推命の暦計算の正確性
**解決策**: 旧暦・節入り日の正確な計算ロジックを実装。必要に応じて外部ライブラリ（lunisolar等）を検討

### 課題4: データベースの初期データ量
**解決策**: JSON形式で初期データを準備し、スクリプトで一括投入。段階的にデータを充実させる

### 課題5: 総合判断の整合性
**解決策**: まずはシンプルな平均値ベースで実装。Phase 2でLLMを導入し、より洗練された解釈を生成

---

## 11. 非機能要件（参考）

### パフォーマンス
- 占い結果の生成時間: 5秒以内（目標）
- データベースクエリの最適化

### 拡張性
- 新しい占い手法の追加が容易
- データ駆動型設計により、コード変更を最小限に

### 保守性
- 明確なモジュール分割
- 命名規則の統一
- ドキュメント整備

### ローカル環境での動作
- インターネット接続不要（LLM未使用時）
- シンプルなセットアップ手順

---

## 12. 今後の拡張可能性

### Phase 2以降で検討する機能
- 出生時刻・出生地の対応（より詳細な西洋占星術）
- 履歴機能（過去の占い結果の保存・比較）
- LLM統合（Claude/OpenAI APIによる自然な解釈文生成）
- グラフ・チャートの視覚化強化
- 九星気学、宿曜占星術などの追加手法
- PDF出力機能
- 相性占い（2人の生年月日を比較）

### Phase 3以降
- 管理画面の実装
- 手法のON/OFF切り替え
- 手法ごとの重み付け設定
- カスタム解釈データの編集機能

---

## 付録: 主要ライブラリ

### 必須ライブラリ
```
Flask==3.0.0
SQLAlchemy==2.0.23
pyswisseph==2.10.3.2
```

### 推奨ライブラリ
```
python-dateutil==2.8.2
pytz==2023.3
```

### 将来的な追加（Phase 2以降）
```
anthropic==0.8.0          # Claude API
openai==1.6.0             # OpenAI API（選択肢）
```

---

## 改訂履歴

| 版 | 日付 | 変更内容 | 作成者 |
|---|------|---------|--------|
| 1.0 | 2025-11-06 | 初版作成 | Claude |

