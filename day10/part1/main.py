from dataclasses import dataclass

@dataclass
class Input:
    desired_state: str
    buttons: list[list[int]]

def parse_input() -> list[Input]: 
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()
    
    inputs: list[Input] = []
    for line in lines:
        sections: list[str] = line.split(' ')
        state: str = sections[0][1:-1] # Remove brackets
        

        buttons: list[list[int]] = []
        for section in sections[1:-1]:
            string: str = section[1:-1] # Remove parenthesis
            nums = [int(num) for num in string.split(',')]
            buttons.append(nums)
        inputs.append(Input(state, buttons))

    return inputs

def apply(curr_state: str, button: list[Input]) -> str:
    new_state: str = curr_state
    for led in button:
        val: str = '#' if new_state[led] == '.' else  '.'
        if led == 0:
            new_state = val + new_state[1:]
        elif led == len(curr_state):
            new_state = new_state[:-1] + val
        else:
            new_state = new_state[0:led] + val + new_state[led+1:]
    return new_state

def solve(input: Input) -> int:
    starting_state = '.' * len(input.desired_state)
    visited_states: set[str] = { starting_state }
    active_states: list[str] = [ starting_state ]

    presses = 1
    while presses < 1000:
        new_states: list[str] = []
        for curr_state in active_states:
            for button in input.buttons:
                new_state = apply(curr_state, button)
                if new_state == input.desired_state:
                    return presses
                elif new_state in visited_states:
                    continue
                visited_states.add(new_state)
                new_states.append(new_state)
        active_states += new_states
        presses += 1
    return presses


inputs: list[Input] = parse_input()
res: list[int] = []
for input in inputs:
    res.append(solve(input))
print(sum(res))