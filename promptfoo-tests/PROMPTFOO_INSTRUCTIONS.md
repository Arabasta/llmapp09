# Promptfoo evaluations

The four suites exercise classify, sentiment, summarize, and intent through
the running backend at `http://localhost:8080`.

```sh
npm ci
npm run eval
```

Individual suites are available as `npm run eval:classify`,
`npm run eval:sentiment`, `npm run eval:summarize`, and
`npm run eval:intent`. Promptfoo is pinned in `package-lock.json`.
