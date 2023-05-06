from typing import List

# Definition of Interval
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def canAttendMeetings(meetings: List[Interval]) -> bool:
    if len(meetings) < 2:
        return True
    sortedMeetings = sorted(meetings, key=lambda meeting: meeting.start)
    previousMeeting = sortedMeetings[0]
    for currentMeeting in sortedMeetings[1:]:
        if currentMeeting.start < previousMeeting.end:
            return False
        previousMeeting = currentMeeting
    return True


print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
meeting1 = Interval(2,10)
meeting2 = Interval(11,15)
day1Meetings = [meeting1, meeting2]
print("canAttendMeetings - ", "[2,10], [11,15]")
print(canAttendMeetings(day1Meetings))
print("##################################################")
meeting3 = Interval(8,10)
meeting4 = Interval(9,12)
day2Meetings = [meeting3, meeting4]
print("canAttendMeetings - ", "[8,10], [9,12]")
print(canAttendMeetings(day2Meetings))
print("##################################################")
print("##################################################")