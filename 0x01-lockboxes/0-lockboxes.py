#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def look_next_opened_box(opened_boxes):
    """Finds the next box that has been opened but not yet checked for keys.
    
    Args:
        opened_boxes (dict): Dictionary with the status and keys of each opened box.
    
    Returns:
        list: List of keys from the next opened box, or None if all opened boxes have been checked.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None

def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked starting from the first box.
    
    Args:
        boxes (list): List of lists, where each sublist contains keys to other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    if len(boxes) <= 1:
        return True

    # Dictionary to track the status and keys of each box
    aux = {0: {'status': 'opened', 'keys': boxes[0]}}
    
    while True:
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                if key < len(boxes) and key not in aux:
                    aux[key] = {'status': 'opened', 'keys': boxes[key]}
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        else:
            break

    return len(aux) == len(boxes)

def main():
    """Tests the canUnlockAll function with sample inputs."""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should print: False

if __name__ == '__main__':
    main()

