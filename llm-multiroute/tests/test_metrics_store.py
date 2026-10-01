import importlib
import json

metrics_module = importlib.import_module("app.monitoring.metrics_store")


def test_corrupt_metrics_file_is_recovered(monkeypatch, tmp_path):
    performance_file = tmp_path / "performance_metrics.json"
    performance_file.write_text("")
    monkeypatch.setattr(metrics_module, "PERFORMANCE_FILE", performance_file)
    monkeypatch.setattr(metrics_module, "METRICS_DIR", tmp_path)

    store = metrics_module.MetricsStore()
    store.record_latency("classify", "test-model", 0.25)

    saved = json.loads(performance_file.read_text())
    assert saved["summary"]["total_requests"] == 1


def test_metrics_write_failure_does_not_break_request(monkeypatch, tmp_path):
    monkeypatch.setattr(metrics_module, "PERFORMANCE_FILE", tmp_path / "performance.json")
    monkeypatch.setattr(metrics_module, "METRICS_DIR", tmp_path)

    def fail_to_open(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(metrics_module.tempfile, "NamedTemporaryFile", fail_to_open)

    store = metrics_module.MetricsStore()
    store.record_latency("classify", "test-model", 0.25)
