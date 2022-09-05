import os


def non_overlap_intervals(tstamps):
    time_covered = 0
    intervals = [0 for i in range(0, int(len(tstamps)/2))]
    on_duty_guards = []
    for count, value in enumerate(tstamps):
        current_time = value['time']
        if len(on_duty_guards) > 0:
            diff = current_time - tstamps[count - 1]['time']
            time_covered += diff
        if value['status'] == 1:
            on_duty_guards.append(value['guard_id'])
        else:
            on_duty_guards.remove(value['guard_id'])
        if len(on_duty_guards) == 1:
            intervals[on_duty_guards[0]] += tstamps[count + 1]['time'] - current_time
    return intervals, time_covered


def max_interval(tstamps):
    intervals, time_covered = non_overlap_intervals(tstamps)
    return (time_covered - min(intervals))


directory = 'Input'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f) as file_in:
            tstamps = []
            num_guards = 0
            for line in file_in:
                x = line.split()
                if (len(x) == 2):
                    tstamps.append({'time': int(x[0]), 'status': 1, 'guard_id': num_guards})
                    tstamps.append({'time': int(x[1]), 'status': 0, 'guard_id': num_guards})
                    num_guards += 1
            tstamps = sorted(tstamps, key=lambda d: d['time'])
        out_file_name = 'Output/'+filename.split('.')[0] + '.out'
        file_out = open(out_file_name, "w+")
        file_out.write(str(max_interval(tstamps)))
        file_out.close()
