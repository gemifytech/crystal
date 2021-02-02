from src.node import app
from src.blockchain import TransactionBlockchain, FeedbackBlockchain, CitationBlockchain

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    tx_chain = TransactionBlockchain()
    fb_chain = FeedbackBlockchain()
    ct_chain = CitationBlockchain()
    app.run(host='0.0.0.0', port=port, debug=True)