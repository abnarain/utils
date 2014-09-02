import matplotlib
matplotlib.rcParams['text.usetex']=True #to force to Type1 font
from matplotlib.figure import Figure
from   matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.font_manager
color= ['black', 'blue', 'green', 'brown', 'red', 'purple', 'cyan', 'magenta', 'orange', 'yellow', 'pink',
        'lime', 'olive', 'chocolate','navy', 'teal', 'gray', 'crimson',  'darkred' , 'darkslategray',
    'violet', 'mediumvioletred' ,'orchid','tomato' , 'coral', 'goldenrod', 'tan', 'peru',  'sienna',
    'rosybrown','darkgoldenrod','navajowhite','darkkhaki','darkseagreen' ,'firebrick','lightsteelblue']


LEGEND_PROP = matplotlib.font_manager.FontProperties(size=6)
fig_width = 12
fig_length = 12.25 
fig_left = 0.12
fig_right = 0.94
fig_bottom = 0.25
fig_top = 0.94
fig_hspace = 0.5

def template_plotter(x_axis_label, y_axis_label,x_axes=[],x_ticks=[],title, outfile_name):
    fig = Figure(linewidth=0.0)
    fig.set_size_inches(fig_width,fig_length, forward=True)
    Figure.subplots_adjust(fig, left = fig_left, right = fig_right, bottom = fig_bottom, top = fig_top, hspace = fig_hspace)

    _subplot = fig.add_subplot(1,1,1)
    _subplot.boxplot(x_axis,notch=0,sym='+',vert=1, whis=1.5)    
    #_subplot.plot(x,y,color='b', linestyle='--', marker='o' ,label='labels')
    a =[i for i in range(1,len(x_ticks)+1)]
    _subplot.set_xticklabels(x_ticks)
    _subplot.set_xticks(a)
    labels=_subplot.get_xticklabels()
    for label in labels:
        label.set_rotation(30)
    _subplot.set_ylabel(y_axis_label,fontsize=36)
    _subplot.set_xlabel(x_axis_label)
    #_subplot.set_ylim()
    #_subplot.set_xlim()
    
    _subplot.set_title(title)
    _subplot.legend(loc='upper left',prop=LEGEND_PROP ,bbox_to_anchor=(0.5, -0.05))
    canvas = FigureCanvasAgg(fig)
    if '.eps' in outfile_name:
        canvas.print_eps(outfile_name, dpi = 110)
    if '.png' in outfile_name:
        canvas.print_figure(outfile_name, dpi = 110)
    outfile_name='EpsilonvsMTU.pdf'
    if '.pdf' in outfile_name:
        canvas.print_figure(outfile_name, dpi = 110)
