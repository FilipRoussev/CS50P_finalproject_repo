from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib import pyplot as plt

def main():
    court()


def court(ax=None, color='black', lw=2, outer_lines=True):
    if ax is None:
        ax = plt.gca()
    # Hoop
    hoop_radius = 45.72 / 2  # Diameter of hoop: 45.72 cm
    hoop = Circle((0, 0), radius=hoop_radius, linewidth=lw, color=color, fill=False)

    # Backboard
    backboard_width = 180
    backboard_height = -1
    backboard = Rectangle((-90, -157.5 + 120), backboard_width, backboard_height, linewidth=lw, color=color)


    # Paint area
    outer_box_width = 490
    outer_box_height = 580
    outer_box = Rectangle((-490 / 2, -157.5), outer_box_width, outer_box_height,
                          linewidth=lw, color=color, fill=False)
    inner_box_width = 360
    inner_box = Rectangle((-360 / 2, -157.5), inner_box_width, outer_box_height,
                          linewidth=lw, color=color, fill=False)
    
    # Free throw arcs
    free_throw_radius = 360
    top_free_throw = Arc((0, 580 - 157.5), free_throw_radius, free_throw_radius, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    bottom_free_throw = Arc((0, 580 - 157.5), free_throw_radius, free_throw_radius, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    
    # Restricted zone
    restricted_radius = 125 * 2
    restricted = Arc((0, 0), restricted_radius, restricted_radius, theta1=0, theta2=180,
                     linewidth=lw, color=color)
    
    # Three-point line
    corner_three_a = Rectangle((-750 + 90, -157.5), 0, 305,
                               linewidth=lw, color=color)
    corner_three_b = Rectangle((750 - 90, -157.5), 0, 305,
                               linewidth=lw, color=color)
    three_point_arc_radius = 675
    three_point_arc = Arc((0, 0), 2 * three_point_arc_radius, 2 * three_point_arc_radius, theta1=11, theta2=167.5,
                          linewidth=lw, color=color)
    
    # Center court
    center_outer_arc_radius = 180
    center_outer_arc = Arc((0, 1400 - 157.5), 2 * center_outer_arc_radius, 2 * center_outer_arc_radius,
                           theta1=180, theta2=0, linewidth=lw, color=color)
    
    # Outer lines
    outer_lines = Rectangle((-750, -157.5), 1500, 1400, linewidth=lw, color=color, fill=False)

    elements = [hoop, backboard, outer_box, inner_box, top_free_throw, bottom_free_throw, restricted, corner_three_a, corner_three_b, three_point_arc, center_outer_arc, outer_lines]



    for element in elements:
        ax.add_patch(element)
        ax.set_aspect(aspect='equal')
        ax.set_axis_off()
        
    return ax



if __name__=="__main__":
    main()