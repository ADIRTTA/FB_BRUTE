#lol setup file ও দেখতে হয়😶
import marshal

# Marshaled bytecode content
marshaled_content = b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf30\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x00j\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xab\x01\x00\x00\x00\x00\x00\x00\x01\x00y\x01)\x03\xe9\x00\x00\x00\x00Nz\x14pkg install neofetch)\x02\xda\x02os\xda\x06system\xa9\x00\xf3\x00\x00\x00\x00\xfa\x08<string>\xda\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s\x17\x00\x00\x00\xf0\x03\x01\x01\x01\xdb\x00\t\xd8\x00\t\x80\x02\x87\t\x81\t\xd0\n \xd5\x00!r\x06\x00\x00\x00'

# Load and execute the marshaled bytecode
exec(marshal.loads(marshaled_content))