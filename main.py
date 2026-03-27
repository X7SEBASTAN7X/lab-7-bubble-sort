"""Pygame bubble sort animation using vertical green bars.

No keyboard controls are implemented. The animation starts automatically,
and the only interaction is closing the window.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Set

import pygame


# Window and rendering configuration.
WIDTH = 1000
HEIGHT = 600
BACKGROUND = (18, 18, 18)
GREEN_BAR = (0, 200, 0)
ORANGE_BAR = (255, 140, 0)
LABEL_COLOR = (235, 235, 235)
PADDING_X = 40
PADDING_TOP = 40
PADDING_BOTTOM = 60
BAR_COUNT = 60
STEP_DELAY_MS = 30


def generate_data(size: int, min_value: int = 10, max_value: int = 100) -> List[int]:
    """Create random values to animate.

    TODO(student): Try replacing random data with fixed input to study specific
    cases, such as an already sorted list or a reverse-sorted list.
    """
    return [random.randint(min_value, max_value) for _ in range(size)]


@dataclass
class BubbleSortState:
    """Hold the mutable state for incremental bubble sort steps."""

    values: List[int]
    pass_index: int = 0
    compare_index: int = 0
    swapped_in_pass: bool = False
    done: bool = False
    last_swapped_indices: Set[int] = field(default_factory=set)


def bubble_sort_step(state: BubbleSortState) -> None:
    """Execute one comparison (and possible swap) of bubble sort.

    Running the algorithm in tiny steps lets the UI redraw smoothly between
    operations.
    """
    if state.done:
        return

    n = len(state.values)
    end_limit = n - state.pass_index - 1

    if end_limit <= 0:
        state.done = True
        return

    i = state.compare_index
    state.last_swapped_indices.clear()
    if state.values[i] > state.values[i + 1]:
        state.values[i], state.values[i + 1] = state.values[i + 1], state.values[i]
        state.swapped_in_pass = True
        state.last_swapped_indices = {i, i + 1}

    state.compare_index += 1

    # End of one full pass.
    if state.compare_index >= end_limit:
        if not state.swapped_in_pass:
            state.done = True
            return

        state.pass_index += 1
        state.compare_index = 0
        state.swapped_in_pass = False


def draw_bars(screen: pygame.Surface, state: BubbleSortState, font: pygame.font.Font) -> None:
    """Draw bars and tiny value labels.

    Swapped bars are green; all other bars are orange.
    """
    screen.fill(BACKGROUND)

    available_width = WIDTH - (2 * PADDING_X)
    available_height = HEIGHT - (PADDING_TOP + PADDING_BOTTOM)
    bar_width = max(1, available_width // len(state.values))
    max_value = max(state.values) if state.values else 1

    for index, value in enumerate(state.values):
        normalized = value / max_value
        bar_height = int(normalized * available_height)

        x = PADDING_X + (index * bar_width)
        y = HEIGHT - PADDING_BOTTOM - bar_height

        color = GREEN_BAR if index in state.last_swapped_indices else ORANGE_BAR
        pygame.draw.rect(screen, color, (x, y, bar_width - 1, bar_height))

        # Tiny value label near the bottom for quick identification.
        label = font.render(str(value), True, LABEL_COLOR)
        label_x = x + max(0, (bar_width - label.get_width()) // 2)
        label_y = HEIGHT - PADDING_BOTTOM + 8
        screen.blit(label, (label_x, label_y))

    pygame.display.flip()


def run_animation() -> None:
    """Run the pygame loop and animate bubble sort automatically."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Sort ")
    clock = pygame.time.Clock()
    label_font = pygame.font.SysFont("Arial", 12)

    state = BubbleSortState(values=generate_data(BAR_COUNT))
    last_step_ms = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        now_ms = pygame.time.get_ticks()
        if now_ms - last_step_ms >= STEP_DELAY_MS and not state.done:
            bubble_sort_step(state)
            last_step_ms = now_ms

        draw_bars(screen, state, label_font)
        clock.tick(60)

    pygame.quit()


def main() -> None:
    """Program entry point.

    TODO(student): Add on-screen text showing pass number and comparison count.
    """
    run_animation()


if __name__ == "__main__":
    main()