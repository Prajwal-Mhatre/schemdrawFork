import schemdraw
import schemdraw.elements as elm
import functools

# Create a function tracer with indentation for better readability
call_depth = 0
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global call_depth
        indent = "  " * call_depth
        print(f"{indent}→ {func.__module__}.{func.__qualname__}")
        call_depth += 1
        result = func(*args, **kwargs)
        call_depth -= 1
        print(f"{indent}← {func.__module__}.{func.__qualname__}")
        return result
    return wrapper

# Patch key methods to trace
original_draw = schemdraw.Drawing.draw
schemdraw.Drawing.draw = trace(original_draw)

original_exit = schemdraw.Drawing.__exit__
schemdraw.Drawing.__exit__ = trace(original_exit)

original_place = schemdraw.elements.Element._place
schemdraw.elements.Element._place = trace(original_place)

original_element_draw = schemdraw.elements.Element._draw
schemdraw.elements.Element._draw = trace(original_element_draw)

original_segment_draw = schemdraw.segments.Segment.draw
schemdraw.segments.Segment.draw = trace(original_segment_draw)

original_figure_plot = schemdraw.backends.svg.Figure.plot
schemdraw.backends.svg.Figure.plot = trace(original_figure_plot)

# This is where the important calls happen - when the with block closes
with schemdraw.Drawing(file='schematic.svg') as d:
    r1 = elm.Resistor().label('100KΩ')
    # At this point, the resistor is created but not yet drawn
    print("\n--- Exiting the with block will trigger drawing and saving ---\n")