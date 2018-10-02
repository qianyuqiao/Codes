import shlex
cmd = 'ovs-vsctl add-port br-int tap7f41c  --  set  Interface tap7f41c external-ids:iface-id=7f41c6c0-3f9a-4d9a-a93b-9e692050be1a'\
        'external-ids:iface-status=active external-ids:attached-mac=fa:16:3e:1b:64:11'

cmd = shlex.split(cmd)
print cmd
