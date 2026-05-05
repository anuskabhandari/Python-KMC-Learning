def log_event(event_type, *args, **kwargs):
    # 1. Check if messages exist
    if not args:
        raise ValueError ("At least one message is required")

    # 2. Convert messages into list
    messages = list(args)

    # 3. Metadata handling
    meta = {}

    # Allowed keys
    allowed_keys = {"timestamp", "user", "priority"}

    # Filter only valid keys
    for key, value in kwargs.items():
        if key in allowed_keys:
            meta[key] = value
        else:
            # handle extra keys safely (merge without conflict)
            meta[key] = value

    # 4. Extra condition: priority = high → add alert
    if meta.get("priority") == "high":
        meta["alert"] = True

        

    # 5. Final dictionary
    return {
        "type": event_type,
        "messages": messages,
        "meta": meta
    }