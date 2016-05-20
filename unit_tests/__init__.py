import sys
import mock

sys.path.append('src')
sys.path.append('src/lib')

# Mock out charmhelpers so that we can test without it.
# also stops sideeffects from occuring.
charmhelpers = mock.MagicMock()
sys.modules['charmhelpers'] = charmhelpers
sys.modules['charmhelpers.core'] = charmhelpers.core
sys.modules['charmhelpers.core.hookenv'] = charmhelpers.core.hookenv
sys.modules['charmhelpers.core.host'] = charmhelpers.core.host
sys.modules['charmhelpers.core.templating'] = charmhelpers.core.templating
sys.modules['charmhelpers.contrib'] = charmhelpers.contrib
sys.modules['charmhelpers.contrib.openstack'] = charmhelpers.contrib.openstack
sys.modules['charmhelpers.contrib.openstack.utils'] = (
    charmhelpers.contrib.openstack.utils)
sys.modules['charmhelpers.contrib.openstack.templating'] = (
    charmhelpers.contrib.openstack.templating)
sys.modules['charmhelpers.contrib.network'] = charmhelpers.contrib.network
sys.modules['charmhelpers.contrib.network.ip'] = (
    charmhelpers.contrib.network.ip)
sys.modules['charmhelpers.fetch'] = charmhelpers.fetch
sys.modules['charmhelpers.cli'] = charmhelpers.cli
sys.modules['charmhelpers.contrib.hahelpers'] = charmhelpers.contrib.hahelpers
sys.modules['charmhelpers.contrib.hahelpers.cluster'] = (
    charmhelpers.contrib.hahelpers.cluster)
