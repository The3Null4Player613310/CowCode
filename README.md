# CowCode
A implementation of MooMooEncode in python.

## Usage

  **A file can be encoded using cow.py.**\
  ex: cat <input_file> | python cow.py >> <output_file>
  
  **A file can be decoded using uncow.py.**\
  ex: cat <input_file> | python uncow.py >> <output_file>
  
  **Files can even be encoded and decoded on the fly.**\
  For example you can use netcat to set up a listen server\
  and pipe through cow.py and uncow.py to encode and decode\
  the data respectivly**.
  
  server: netcat -l -p <server_port> | python uncow.py >> <output_file>\
  client: cat <input_file> | python cow.py | netcat -c <ip_address> <server_port>
