from sof import *
from indeed import *
from save import *

indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()

jobs = indeed_jobs + sof_jobs

save_to_csv(jobs)