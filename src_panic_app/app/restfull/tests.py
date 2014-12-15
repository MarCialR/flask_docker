json_tests = [

{
'name': 'TestDefaultFirewallRules',
'tipe': 'command&output',
'command': "gcloud compute firewall-rules list --project panic-tests",
'expected': """NAME                   NETWORK SRC_RANGES    RULES                        SRC_TAGS TARGET_TAGS
default-allow-http     default 0.0.0.0/0     tcp:80                                http-server
default-allow-icmp     default 0.0.0.0/0     icmp
default-allow-internal default 10.240.0.0/16 tcp:1-65535,udp:1-65535,icmp
default-allow-rdp      default 0.0.0.0/0     tcp:3389
default-allow-ssh      default 0.0.0.0/0     tcp:22
"""
},


{
'name': 'TestDefaultFirewallEmpty',
'tipe': 'command&output',
'command': "gcloud compute firewall-rules list --project panic-tests",
'expected': 
"""
"""
}
,


{
'name': 'Borrame',
'tipe': 'command&output',
'command': "gcloud compute firewall-rules --project panic-tests list",
'expected': 
"""NAME                   NETWORK SRC_RANGES    RULES                        SRC_TAGS TARGET_TAGS
default-allow-http     default 0.0.0.0/0     tcp:80                                http-server
default-allow-icmp     default 0.0.0.0/0     icmp
default-allow-internal default 10.240.0.0/16 tcp:1-65535,udp:1-65535,icmp
default-allow-rdp      default 0.0.0.0/0     tcp:3389
default-allow-ssh      default 0.0.0.0/0     tcp:22
"""
}
,

]

for i in json_tests:
	i['menu'] = 'computeengine'
