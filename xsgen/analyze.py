"""A simple analysis plugin for xsgen to aid in output validation.

Analysis Plugin API
===================
"""

from xsgen.plugins import Plugin

class XSGenPlugin(Plugin):
    """This class cleans up after xsgen."""

    rcdocs = {
        "analyze_omc": "If set, will plot the group flux generated by OpenMC."
        }

    def update_argparser(self, parser):
        parser.add_argument("--analyze_omc", action="store_true", dest="analyze_omc",
            help="Launches the xsgen ui.")
        parser.add_argument("-c", "--clean", action="store_true", dest="clean",
            help="Cleans the reactor directory of current files.")
        parser.add_argument('--formats', dest='formats', help=self.rcdocs['formats'],
                            nargs='+')
        parser.add_argument('--threads', dest='threads', help=self.rcdocs['threads'],
                            type=int)
        parser.add_argument('--outfiles', dest='outfiles', type=list, help=self.rcdocs['outfiles'],
                            nargs='+')
        parser.add_argument('--is-thermal', dest='is_thermal', type=bool,
                            help=self.rcdocs['is_thermal'])

    def execute(self, rc):
        """Leaves the reactor directory if --cwd was not specified."""

        if not rc.get('CWD'):
            os.chdir('..')
        print("\a")
