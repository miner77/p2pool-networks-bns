from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    


bonuscoin=math.Object( 
        PARENT=networks.nets['bonuscoin'], 
        SHARE_PERIOD=10, 
        CHAIN_LENGTH=24*60*60//10, 
        REAL_CHAIN_LENGTH=24*60*60//10, 
        TARGET_LOOKBEHIND=200, 
        SPREAD=15, 
        IDENTIFIER='76d3f6dce9c83b1d'.decode('hex'),
        PREFIX='68420a6e16cacd84'.decode('hex'),
        P2P_PORT=55000, 
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=55001, 
        BOOTSTRAP_ADDRS='bonuscoin.net 67.231.54.19 148.251.12.124'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Bitcoin to >=0.8.5!' if v < 80500 else None,
        
    )

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
