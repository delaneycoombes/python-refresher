import subprocess


SCRIPT = "../print_fires.py"
DATA = "../data/test_fires.csv"


def run_test(args):
    return subprocess.run(
        ["python3", SCRIPT] + args,
        capture_output=True,
        text=True,
    )


# Exit code tests
def test_exit_success_no_operation():
    result = run_test(["Brazil", "0", "2", DATA])
    assert result.returncode == 0


def test_exit_success_mean():
    result = run_test(
        ["Brazil", "0", "2", DATA, "--operation", "mean"]
    )
    assert result.returncode == 0


def test_exit_success_median():
    result = run_test(
        ["Brazil", "0", "2", DATA, "-o", "median"]
    )
    assert result.returncode == 0


def test_exit_success_std():
    result = run_test(
        ["Brazil", "0", "2", DATA, "--operation", "std"]
    )
    assert result.returncode == 0


def test_exit_missing_args():
    result = run_test([])
    assert result.returncode == 2


def test_exit_bad_operation():
    result = run_test(
        ["Brazil", "0", "2", DATA, "--operation", "foo"]
    )
    assert result.returncode == 2


# Raw list output tests
def test_raw_brazil():
    result = run_test(["Brazil", "0", "2", DATA])
    assert result.returncode == 0
    assert "100" in result.stdout
    assert "150" in result.stdout
    assert "200" in result.stdout


def test_raw_usa():
    result = run_test(["USA", "0", "2", DATA])
    assert result.returncode == 0
    assert "20" in result.stdout
    assert "25" in result.stdout


def test_raw_unknown_country():
    result = run_test(["Nowhere", "0", "2", DATA])
    assert result.returncode == 0
    assert "[]" in result.stdout


# Operation tests
def test_mean_brazil():
    result = run_test(
        ["Brazil", "0", "2", DATA, "--operation", "mean"]
    )
    assert result.returncode == 0
    assert "150.0" in result.stdout


def test_median_brazil():
    result = run_test(
        ["Brazil", "0", "2", DATA, "-o", "median"]
    )
    assert result.returncode == 0
    assert "150.0" in result.stdout


def test_std_brazil():
    result = run_test(
        ["Brazil", "0", "2", DATA, "--operation", "std"]
    )
    assert result.returncode == 0
    assert result.stdout


def test_mean_usa():
    result = run_test(
        ["USA", "0", "2", DATA, "--operation", "mean"]
    )
    assert result.returncode == 0
    assert "22.5" in result.stdout


def test_mean_unknown():
    result = run_test(
        ["Nowhere", "0", "2", DATA, "--operation", "mean"]
    )
    assert result.returncode == 0
    assert "[]" in result.stdout
