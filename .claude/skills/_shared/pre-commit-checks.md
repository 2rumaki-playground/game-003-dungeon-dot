# コミット前チェック

各コミットの前に以下を**リポジトリルートから順に**実行し、問題があれば修正する:

1. `task format` — フォーマット適用
2. `task lint` — リントチェック
3. `task typecheck` — 型チェック
4. `task deps:check` — 依存方向チェック
5. `task test` — ユニットテスト全通過を確認
