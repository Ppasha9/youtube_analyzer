import matplotlib.pyplot as plt


def plot_pie_chart(labels, sizes, explode):
    fig_pie, ax_pie = plt.subplots()

    wp = {'linewidth': 1, 'edgecolor': "green"}
    tp = {'color': 'black'}

    wedges, texts, autotexts = ax_pie.pie(sizes,
                                          shadow=True,
                                          explode=explode,
                                          autopct="%1.1f%%",
                                          startangle=90,
                                          wedgeprops=wp,
                                          textprops=tp)

    ax_pie.legend(wedges, labels, loc="best")
    plt.setp(autotexts, size=8, weight="bold")
    ax_pie.axis('equal')

    plt.show()
