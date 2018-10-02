from kombu.entity import Exchange,Queue 
from kombu.messaging import Producer
from kombu.connection import Connection
MSG= {'_context_request_id': 'req-623f4e52-600c-4e48-bbb7-6aea4d28f9f8', 
'_context_user_name': None, 
'args': {'agent_state': {'agent_state': {'binary': 'neutron-openvswitch-agent', 'start_flag': True, 'topic': 'N/A', 'host': 'myhost', 'agent_type': 'Open vSwitch agent', 'configurations': {'tunnel_types': [], 'tunneling_ip': '', 'bridge_mappings': {'physnet1': 'br-eth1'}, 'l2_population': False, 'devices': 0}}}, 'time': '2018-04-15T13:56:55.047384'}, 'namespace': None, '_unique_id': 'bd14f8a214ba46b480b1e9f87feb18f8', 
'_context_timestamp':'2014', 
'_context_user_id': '123456', 'method': 'report_state'}

def main():
    
    connection = Connection('amqp://guest:767918@localhost:5672//')
    _channel=connection.channel()
    _exchange= Exchange('neutron',type='topic')

    pro= Producer(channel=_channel,exchange=_exchange,routing_key='q-plugin')
    pro.publish(MSG)

if __name__ == '__main__':
    main()
