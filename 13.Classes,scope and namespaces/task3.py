
#Task 3

#TV controller

#Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#The default channel turned on before all commands is №1.

#Your task is to create the TVController class and methods described above.




class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[0]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_channel_index = N - 1
            return self.channels[self.current_channel_index]
        else:
            return "Channel does not exist"

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, N):
        if type(N) == int:
            return "Yes" if 1 <= N <= len(self.channels) else "No"
        elif type(N) == str:
            return "Yes" if N in self.channels else "No"
        else:
            return "Invalid argument"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())  
print(controller.last_channel())  
print(controller.turn_channel(1))  
print(controller.next_channel())  
print(controller.previous_channel())  
print(controller.current_channel())  
print(controller.is_exist(4))  
print(controller.is_exist("BBC"))  
