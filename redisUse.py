import redis

redisClient = redis.StrictRedis(host='49.233.181.190', port=6379, db=0, password=666666)

def addUserInput(userInput):
    redisClient.rpush('user_data', userInput)

def getAllUserInputs():
    # Retrieve all user inputs from the list
    user_inputs = redisClient.lrange('user_data', 0, -1)
    return [input_data.decode('utf-8') for input_data in user_inputs]

def getInputCount():
    # Get the length (size) of the list
    return redisClient.llen('user_data')

def recordResult(result):
    redisClient.hincrby('result_frequencies', result, 1)

def getFrequency(result):
    # Get the frequency of the given result
    frequency = redisClient.hget('result_frequencies', result)
    return int(frequency) if frequency else 0

def getAllFrenquency():
    result = ["there has been "+str(getInputCount())+" inputs"]
    for key in redisClient.hkeys('result_frequencies'):
        st = key.decode('utf-8') + " occured -> " + str(getFrequency(key)) + " times"
        print(st)
        result.append(st)
    return result

