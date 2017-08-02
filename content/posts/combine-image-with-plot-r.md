title: Place images next to plots in R (Cowplot)
date: 2017-08-02
tags:
  - R
short_description: >
  Make publication ready figures by putting images (such as diagrams) next to
  your ggplot2 graphs using cowplot.

![Trial logger screenshot]({{ url_for('static', filename='blog-images/example_r_figure.png') }})

I couldn't find an easy way to do this but I thought it would be pretty helpful,
so here's a function that does it.

Source code:

    :::r
    library(png)
    library(grid)
    library(tidyverse)
    library(cowplot)

    # generate random data
    my.data <- data.frame(x = c(1:10), y = rnorm(10))

    # plot random data
    g <- ggplot(my.data, aes(x = x, y = y)) +
      geom_line()


    # define plot png function
    plot_png <- function(fname, interpolated = TRUE){

      img <- readPNG(fname) %>%
        rasterGrob(interpolate = interpolated)# enable/disable linear interpolation
      ggplot() +
        annotation_custom(img,
                          xmin = -Inf,
                          xmax = Inf,
                          ymin = -Inf,
                          ymax = Inf)

    }

    # create our ggplot-compatible png
    img <- plot_png("eyediagram.png")

    # plot images together in grid
    plot_grid(g, img, labels = letters)
