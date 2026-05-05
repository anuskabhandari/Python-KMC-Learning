# event- logger system by the sudan sir read it and understand it
def log_event(event_type, *args , ** kwargs):
    pass
    if not isinstance (event_type , str):
        return{
            "error" : "Event type should be string."
        }
    if len(args)<=0:
        {
            "error" : "Provide at least one message"
        }
    if kwargs ['priority'] == "high":
        kwargs['alert'] = True

    return {
        "type": event_type,
        "messages": list(args),
        "meta": kwargs
    }

print(log_event (
     1,
    "name r is not defined",
    "type error cannot add str and int",
     timestamp = "2026-03-21",
     user = "root",
     priority = "low"))

print(log_event (
     "ERROR",
    "name r is not defined",
    "type error cannot add str and int",
     timestamp = "2026-03-21",
     user = "root",
     priority = "high"))
 

## return garda sappai standard ma hunu parxa all in same datatype