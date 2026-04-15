from .config import SAFE
from .sign import sign
from .utils import load_contract

DADDY = load_contract("0x4e8341C77c94cCE982AB96d92BB28D69f4638290")
REGISTRY = load_contract("0xA6D5efF88aB2D192db11A32912c346c8c0AFe125")

@sign()
def endorse():
    # lender = "0xA967FcDb8a2bEF38caaB6131169c9D45be550Db0"
    # trove_manager = "0xAA1ec58c0Ad8eeDED77322d552b12759CAa0c1Cc"
    ENS = load_contract("0xa58E81fe9b61B5c3fE2AFD33CF304c454AbFc7Cb")
    print("Accepting ownership of the Safe...")
    DADDY.accept_ownership()
    print("Setting ENS name...")
    ENS.setName("stepdaddy.flexmeow.eth")

    # // // Accept Lender management
    # // DADDY.execute(address(_lender), abi.encodeWithSelector(ITokenizedStrategy.acceptManagement.selector), 0, true);

    # // // Endorse market
    # // DADDY.execute(address(REGISTRY), abi.encodeWithSelector(IRegistry.endorse.selector, _troveManager), 0, true);
    # 0xAA1ec58c0Ad8eeDED77322d552b12759CAa0c1Cc
