from .config import SAFE
from .sign import sign
from .utils import load_contract

DADDY = load_contract("0x4e8341C77c94cCE982AB96d92BB28D69f4638290")
REGISTRY = load_contract("0xA6D5efF88aB2D192db11A32912c346c8c0AFe125")

@sign()
def endorse():
    lender = load_contract("0xA967FcDb8a2bEF38caaB6131169c9D45be550Db0")
    trove_manager = load_contract("0xAA1ec58c0Ad8eeDED77322d552b12759CAa0c1Cc")

    # accept lender management
    DADDY.execute(lender.address, lender.acceptManagement.encode_input())

    # endorse market
    DADDY.execute(REGISTRY.address, REGISTRY.endorse.encode_input(trove_manager.address))

@sign()
def set_ens_name():
    ens = load_contract("0xa58E81fe9b61B5c3fE2AFD33CF304c454AbFc7Cb")
    ens.setName("daddy.flexmeow.eth")