import sys
# Usage:
# python script_name.py 'model name' 'cpu cores' flags

# NOTE: only works on linux machines!


def get_cpu_info() -> dict:
  infos: dict = {}
  cpu_info = open('/proc/cpuinfo', 'r')
  for line in cpu_info:
    info: str = line.split(':')
    if len(info) == 2:
      infos[info[0].strip()] = info[1].strip()
  return infos


n = len(sys.argv) 
infos = get_cpu_info()
for i in range(1, n): 
  entry = sys.argv[i]
  if entry in infos:
    print(infos[entry])
  else:
    print('"{}" not found.'.format(entry))
