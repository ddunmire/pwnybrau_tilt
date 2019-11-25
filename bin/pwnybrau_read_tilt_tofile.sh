
# Set up environment
export logfile_prefix="/opt/pwnybrau_tilt/logs/pwnybrau_tilt_measurements"
export loglevel="INFO"

# execute sevice
python3 pwnybrau_read_tilt.py --logfile=$logfile_prefix --loglevel=$loglevel
