import Function.Base

import utils.config
from utils.config import Config
import logging


def select_flow(self, branch, flow):
    # 寻找Flow
    path = Config(utils.config.CONFIG_FLOW_PATH).get(branch)[flow]
    print("------------debug info--------------Flow.py", branch, flow, ",flow path is", path)
    logging.debug('branch=' + branch + 'flow=' + flow + 'path=' + path)
    Function.Base.wait_element(self, "xpath", path)
    Function.Base.clickT(self, "xpath", path)

