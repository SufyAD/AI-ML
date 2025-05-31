import re

def get_session_id(session_link: str):    
    if not isinstance(session_link, str):
        return None 
    regex_pattern = r"sessions/(.*?)/contexts/"
    match = re.search(regex_pattern, session_link)

    if match:
        return match.group(1) # group(1) contains the content of the first capturing group
    else:
        return None     


def get_str_from_dict(order: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in order.items()])
    return result
    
# --- Example Usage ---
# if __name__ == "__main__":
#     link1 = "projects/foodpanda-vlny/locations/global/agent/sessions/e6e8a808-e5d0-2e48-cb17-619c9cc2cad7/contexts/ongoing-order"
#     link2 = "another/path/to/sessions/a1b2c3d4-e5f6-7890-1234-567890abcdef/contexts/some-context"
#     link3 = "no/session/id/here"
#     link4 = "projects/foodpanda-vlny/locations/global/agent/sessions/invalid-id/contexts/ongoing-order"
#     link5 = "projects/foodpanda-vlny/locations/global/agent/sessions/e6e8a808-e5d0-2e48-cb17-619c9cc2cad7" # Missing /contexts/

#     print(f"Link 1: {link1}")
#     link = get_session_id(link1)
#     print(f"Extracted Session ID: {link}") # Expected: e6e8a808-e5d0-2e48-cb17-619c9cc2cad7
