from click.testing import CliRunner
from halocli.cli import start,cli
from unittest import TestCase

class TestUtil(TestCase):

    builder = start(False)
    runner = CliRunner()

    def test_cli_base(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, [])
        print('r='+str(result))
        expected_output_log = 'Usage: cli [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 0
        assert result.output.startswith(expected_output_log)

    def test_cli_base1(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["--debug","info"])
        print('r='+str(result.output))
        expected_output_log = 'Debug mode is on'
        assert result.exit_code == 0
        #assert result.output.startswith(expected_output_log)

    def test_cli_base2(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-v","info"])
        print('r='+str(result.output))
        expected_output_log = 'Click Version'
        assert result.exit_code == 0
        #assert result.output.startswith(expected_output_log)

    def test_cli_base3(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-a","info"])
        print('r='+str(result))
        expected_output_log = 'Usage: cli info [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 0
        assert result.output.startswith(expected_output_log)

    def test_cli_base4(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-s","info"])
        print('r='+str(result))
        expected_output_log = 'Usage: cli info [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 2
        #assert result.output.startswith(expected_output_log)

    def test_cli_base41(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-s",".\\abc.json","info"])
        print('r='+str(result.output))
        expected_output_log = 'settings file'
        assert result.exit_code == 0
        #assert result.output.startswith(expected_output_log)

    def test_cli_base5(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-q","info"])
        print('r='+str(result))
        expected_output_log = 'Usage: cli info [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 0
        assert result.output.startswith(expected_output_log)

    def test_cli_base6(self):
        print('test_cli_base')
        #start(False)
        result = self.runner.invoke(cli, ["-r","info"])
        print('r='+str(result.output))
        expected_output_log = 'Verbosity: True'
        assert result.exit_code == 0
        #assert result.output.startswith(expected_output_log)

    def test_cli_valid(self):
        print('test_cli_validate')
        #start(False)
        result = self.runner.invoke(cli, ['validate'])
        print('r='+str(result))
        expected_output_log = 'Usage: cli validate [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 0
        print("r="+result.output)
        assert result.output.startswith(expected_output_log)

    def test_cli_valid_test(self):
        print('test_cli_validate test')
        #start(False)
        result = self.runner.invoke(cli, ['validate','test'])
        print('r='+str(result))
        expected_output_log = 'Usage: cli validate [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 0
        print("r="+result.output)
        #assert result.output.startswith(expected_output_log)

    def test_cli_valid_valid(self):
        print('test_cli_validate valid')
        #start(False)
        result = self.runner.invoke(cli, ['validate','valid'])
        print('r='+str(result))
        expected_output_log = 'Usage: cli validate [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 2
        print("r="+result.output)
        #assert result.output.startswith(expected_output_log)

    def test_cli_valid_valid_v(self):
        print('test_cli_validate valid -a')
        #start(False)
        result = self.runner.invoke(cli, ['validate','valid','-a','x'])
        print('r='+str(result))
        expected_output_log = 'Usage: cli validate [OPTIONS] COMMAND [ARGS]...'
        assert result.exit_code == 2
        print("r="+result.output)
        #assert result.output.startswith(expected_output_log)

    def test_util_1(self):
        print('test_util_1 valid -a')
        #start(False)
        from halocli.util import Util
        expected_output_log = "plugin package: pandas not installed"
        try:
            result = Util.check_package_in_env("pandas")
            print("r=" + str(result))
        except Exception as e:
            print("e=" + str(e))
            assert str(e) == expected_output_log

    def test_util_2(self):
        print('test_util_1 valid -a')
        # start(False)
        from halocli.util import Util
        result = Util.check_package_in_env("halo-test-plugin")
        print("r=" + str(result))
        expected_output = 1
        assert len(result) == expected_output
