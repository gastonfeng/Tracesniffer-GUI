from PayloadData import *

## @package ProtoSpec
#  ProtoSpec provides a lookup-dictionary in both way (ID -> Cleartext-Name and vice cersa) 
#  according to the TSP documentation


## Lookup dictionary. Resolves a numerical ID to a cleartext name
tspDict = {
        0: ('ID_START',None,False),
        1: ('ID_END',None,False),
        2: ('ID_TASK_SWITCHED_IN',Payload1,True),
        3: ('ID_INCREASE_TICK_COUNT',None,False),
        4: ('ID_LOW_POWER_IDLE_BEGIN',None,False),
        5: ('ID_LOW_POWER_IDLE_END',None,False),
        6: ('ID_TASK_SWITCHED_OUT',Payload1,True),
        7: ('ID_TASK_PRIORITY_INHERIT',Payload2,True),
        8: ('ID_TASK_PRIORITY_DISINHERIT',Payload2,True),
        9: ('ID_BLOCKING_ON_QUEUE_RECEIVE',Payload2,True),
        10: ('ID_BLOCKING_ON_QUEUE_SEND',Payload2,True),
        11: ('ID_MOVED_TASK_TO_READY_STATE',Payload1,True),
        12: ('ID_POST_MOVED_TASK_TO_READY_STATE',Payload1,True),
        13: ('ID_QUEUE_CREATE',Payload1,True),
        14: ('ID_QUEUE_CREATE_FAILED',Payload1,False),
        15: ('ID_CREATE_MUTEX',Payload1,True),
        16: ('ID_CREATE_MUTEX_FAILED',Payload0,False),
        17: ('ID_GIVE_MUTEX_RECURSIVE',Payload2,True),
        18: ('ID_GIVE_MUTEX_RECURSIVE_FAILED',Payload2,True),
        19: ('ID_TAKE_MUTEX_RECURSIVE',Payload2,True),
        20: ('ID_TAKE_MUTEX_RECURSIVE_FAILED',Payload2,True),
        21: ('ID_CREATE_COUNTING_SEMAPHORE',Payload0,True),
        22: ('ID_CREATE_COUNTING_SEMAPHORE_FAILED',Payload0,False),
        23: ('ID_QUEUE_SEND',Payload2,True),
        24: ('ID_QUEUE_SEND_FAILED',Payload2,True),
        25: ('ID_QUEUE_RECEIVE',Payload2,True),
        26: ('ID_QUEUE_PEEK',Payload2,True),
        27: ('ID_QUEUE_PEEK_FROM_ISR',Payload2,True),
        28: ('ID_QUEUE_RECEIVE_FAILED',Payload2,True),
        29: ('ID_QUEUE_SEND_FROM_ISR',Payload2,True),
        30: ('ID_QUEUE_SEND_FROM_ISR_FAILED',Payload2,True),
        31: ('ID_QUEUE_RECEIVE_FROM_ISR',Payload2,True),
        32: ('ID_QUEUE_RECEIVE_FROM_ISR_FAILED',Payload2,True),
        33: ('ID_QUEUE_PEEK_FROM_ISR_FAILED',Payload2,True),
        34: ('ID_QUEUE_DELETE',Payload0,True),
        35: ('ID_TASK_CREATE',Payload1,True),
        36: ('ID_TASK_CREATE_FAILED',Payload0,False),
        37: ('ID_TASK_DELETE',Payload1,True),
        38: ('ID_TASK_DELAY_UNTIL',Payload3,True),
        39: ('ID_TASK_DELAY',Payload3,True),
        40: ('ID_TASK_PRIORITY_SET',Payload2,True),
        41: ('ID_TASK_SUSPEND',Payload1,True),
        42: ('ID_TASK_RESUME',Payload1,True),
        43: ('ID_TASK_RESUME_FROM_ISR',Payload1,True),
        44: ('ID_TASK_INCREMENT_TICK',Payload0,False),
        45: ('ID_TIMER_CREATE',None,False),
        46: ('ID_TIMER_CREATE_FAILED',None,False),
        47: ('ID_TIMER_COMMAND_SEND',None,False),
        48: ('ID_TIMER_EXPIRED',None,False),
        49: ('ID_TIMER_COMMAND_RECEIVED',None,False),
        50: ('ID_MALLOC',Payload2,False),
        51: ('ID_FREE',Payload2,False),
        52: ('ID_EVENT_GROUP_CREATE',None,False),
        53: ('ID_EVENT_GROUP_CREATE_FAILED',None,False),
        54: ('ID_EVENT_GROUP_SYNC_BLOCK',None,False),
        55: ('ID_EVENT_GROUP_SYNC_END',None,False),
        56: ('ID_EVENT_GROUP_WAIT_BITS_BLOCK',None,False),
        57: ('ID_EVENT_GROUP_WAIT_BITS_END',None,False),
        58: ('ID_EVENT_GROUP_CLEAR_BITS',None,False),
        59: ('ID_EVENT_GROUP_CLEAR_BITS_FROM_ISR',None,False),
        60: ('ID_EVENT_GROUP_SET_BITS',None,False),
        61: ('ID_EVENT_GROUP_SET_BITS_FROM_ISR',None,False),
        62: ('ID_EVENT_GROUP_DELETE',None,False),
        63: ('ID_PEND_FUNC_CALL',None,False),
        64: ('ID_PEND_FUNC_CALL_FROM_ISR',None,False),
        65: ('ID_QUEUE_REGISTRY_ADD',None,True),
        66: ('ID_TASK_NOTIFY_TAKE_BLOCK',None,True),
        67: ('ID_TASK_NOTIFY_TAKE',None,True),
        68: ('ID_TASK_NOTIFY_WAIT_BLOCK',None,True),
        69: ('ID_TASK_NOTIFY_WAIT',None,True),
        70: ('ID_TASK_NOTIFY',None,True),
        71: ('ID_TASK_NOTIFY_FROM_ISR',None,True),
        72: ('ID_TASK_NOTIFY_GIVE_FROM_ISR',None,True),
        73: ('ID_CUSTOM_MARKER_1',Payload1,False),
        74: ('ID_CUSTOM_MARKER_2',Payload1,False),
        75: ('ID_CUSTOM_MARKER_3',Payload1,False),
        76: ('ID_CUSTOM_MARKER_4',Payload1,False),
        77: ('ID_CUSTOM_MARKER_5',Payload1,False),
        78: ('RESERVED',None,False),
        79: ('RESERVED',None,False),
        80: ('RESERVED',None,False),
        81: ('RESERVED',None,False),
        82: ('RESERVED',None,False),
        83: ('RESERVED',None,False),
        84: ('RESERVED',None,False),
        85: ('RESERVED',None,False),
        86: ('RESERVED',None,False),
        87: ('RESERVED',None,False),
        88: ('RESERVED',None,False),
        89: ('RESERVED',None,False),
        90: ('RESERVED',None,False),
        91: ('RESERVED',None,False),
        92: ('RESERVED',None,False),
        93: ('RESERVED',None,False),
        94: ('RESERVED',None,False),
        95: ('RESERVED',None,False),
        96: ('RESERVED',None,False),
        97: ('RESERVED',None,False),
        98: ('RESERVED',None,False),
        99: ('RESERVED',None,False),
        100: ('RESERVED',None,False),
        101: ('ID_ERROR_STREAM_FIFO_FULL',Payload0,False),
        102: ('ID_ERROR_RECEIVE_FIFO_FULL',Payload0,False),
        103: ('RESERVED',None,False),
        104: ('RESERVED',None,False),
        105: ('RESERVED',None,False),
        106: ('RESERVED',None,False),
        107: ('RESERVED',None,False),
        108: ('RESERVED',None,False),
        109: ('RESERVED',None,False),
        110: ('RESERVED',None,False),
        111: ('RESERVED',None,False),
        112: ('RESERVED',None,False),
        113: ('RESERVED',None,False),
        114: ('RESERVED',None,False),
        115: ('RESERVED',None,False),
        116: ('RESERVED',None,False),
        117: ('RESERVED',None,False),
        118: ('RESERVED',None,False),
        119: ('RESERVED',None,False),
        120: ('RESERVED',None,False),
        121: ('RESERVED',None,False),
        122: ('RESERVED',None,False),
        123: ('RESERVED',None,False),
        124: ('RESERVED',None,False),
        125: ('RESERVED',None,False),
        126: ('RESERVED',None,False),
        127: ('RESERVED',None,False),
        128: ('RESERVED',None,False),
        129: ('RESERVED',None,False),
        130: ('RESERVED',None,False),
        131: ('RESERVED',None,False),
        132: ('RESERVED',None,False),
        133: ('RESERVED',None,False),
        134: ('RESERVED',None,False),
        135: ('RESERVED',None,False),
        136: ('RESERVED',None,False),
        137: ('RESERVED',None,False),
        138: ('RESERVED',None,False),
        139: ('RESERVED',None,False),
        140: ('RESERVED',None,False),
        141: ('RESERVED',None,False),
        142: ('RESERVED',None,False),
        143: ('RESERVED',None,False),
        144: ('RESERVED',None,False),
        145: ('RESERVED',None,False),
        146: ('RESERVED',None,False),
        147: ('RESERVED',None,False),
        148: ('PACKETID_ERROR',Payload0,False),
        149: ('ERROR_START',Payload0,False),
        150: ('ERROR_STOP',Payload0,False),
        151: ('ID_OBJECT_LIST',None,False), # Handled separately in SnifferReader due to highly dynamic nature of structure
        152: ('ID_SNIFF_FILTER',None,False),
        153: ('',None,False),
        154: ('',None,False),
        155: ('',None,False),
        156: ('',None,False),
        157: ('',None,False),
        158: ('',None,False),
        159: ('',None,False),
        160: ('',None,False),
        161: ('',None,False),
        162: ('',None,False),
        163: ('',None,False),
        164: ('',None,False),
        165: ('',None,False),
        166: ('',None,False),
        167: ('',None,False),
        168: ('',None,False),
        169: ('',None,False),
        170: ('',None,False),
        171: ('',None,False),
        172: ('',None,False),
        173: ('',None,False),
        174: ('',None,False),
        175: ('',None,False),
        176: ('',None,False),
        177: ('',None,False),
        178: ('',None,False),
        179: ('',None,False),
        180: ('',None,False),
        181: ('',None,False),
        182: ('',None,False),
        183: ('',None,False),
        184: ('',None,False),
        185: ('',None,False),
        186: ('',None,False),
        187: ('',None,False),
        188: ('',None,False),
        189: ('',None,False),
        190: ('',None,False),
        191: ('',None,False),
        192: ('',None,False),
        193: ('',None,False),
        194: ('',None,False),
        195: ('',None,False),
        196: ('',None,False),
        197: ('',None,False),
        198: ('',None,False),
        199: ('',None,False),
        200: ('',None,False),
        201: ('',None,False),
        202: ('',None,False),
        203: ('',None,False),
        204: ('',None,False),
        205: ('',None,False),
        206: ('',None,False),
        207: ('',None,False),
        208: ('',None,False),
        209: ('',None,False),
        210: ('',None,False),
        211: ('',None,False),
        212: ('',None,False),
        213: ('',None,False),
        214: ('',None,False),
        215: ('',None,False),
        216: ('',None,False),
        217: ('',None,False),
        218: ('',None,False),
        219: ('',None,False),
        220: ('',None,False),
        221: ('',None,False),
        222: ('',None,False),
        223: ('',None,False),
        224: ('',None,False),
        225: ('',None,False),
        226: ('',None,False),
        227: ('',None,False),
        228: ('',None,False),
        229: ('',None,False),
        230: ('',None,False),
        231: ('',None,False),
        232: ('',None,False),
        233: ('',None,False),
        234: ('',None,False),
        235: ('',None,False),
        236: ('',None,False),
        237: ('',None,False),
        238: ('',None,False),
        239: ('',None,False),
        240: ('',None,False),
        241: ('',None,False),
        242: ('',None,False),
        243: ('',None,False),
        244: ('',None,False),
        245: ('',None,False),
        246: ('',None,False),
        247: ('',None,False),
        248: ('',None,False),
        249: ('',None,False),
        250: ('',None,False),
        251: ('',None,False),
        252: ('',None,False),
        253: ('',None,False),
        254: ('',None,False),
        255: ('',None,False),
}

## A list of all available informationIDs
IDList = []
for k,v in tspDict.items():
    IDList.append(v[0])

## Reverse-lookup dictionary. Resolves a Cleartextname to a numerical ID
tspName2Id={}
for id,(name,type,objrel) in tspDict.items():
    if name: tspName2Id[name]=id