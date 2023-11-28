# Origami Wireframe Polyhedra

## Intro

This work is motivated when I looked into finding a modular origami design for all the uniform polyhedra and didn't find anything comprehensive on my first pass.  I decided upon a wireframe model because of the clean look and I realized that the only alteration that would be needed to fold all the Archimedean solids would be to change the angle that the units come together.  I also knew that these units have been designed to create a variety of polyhedra such as found in Tomoko Fuse's "Open Frame II Unit" in **Unit Origami: Multidimensional Transformations**, or David Mitchell's "Outline Dodecahedron" in **Mathematical Origami**, or the model for Thomas Hull's "Five Intersecting Tetrahedra".  I was a little intimidated on how to fold the angles correctly and exactly, until I noticed how not even the angles for the "Outline Dodecahedron" in **Mathematical Origami** are mathematically exact.  Knowing the quality of that model with only using a simple but approximate angle convinced me that finding the mathematically exact folds for these polyhedra was misguided.

I want a place to save notes as to how I did it since otherwise I have nothing written down and will invariably forget.  After completing the Archimedean solids in February/March 2023, I was done for the moment but knew I would want to develop it further later.  At some point I will probably do the Johnson solids but that doesn't require anything new compared to the Archimedean solids - beyond the frustration of developing a color scheme.  I decided to instead attempt the Catalan solids.  The biggest motivator to develop this repository is due to the fact that each of these polyhedra have (comparatively to the Archimedean solids) arbitrary angles and lengths.  Each solid requires multiple unique sets of folds and streamlining the process and saving the results is more important.

The added benefit of collecting this on GitHub is that I can share and showcase this work.  Enjoy!

## Philosophy

- **Everything is approximate**

    - I know I have limits to how exact each of my folds are.  There is no point in creating a mathematically _exact_ fold if it is complicated - any fold in practice is inexact.

- **Fewer folds the better**

    - Errors are compounded by multiple folds.  Fewer folds, more exact results.
    - Modular origami can require many units.  Fewer folds, faster results.
    - More folds can lead to spurious creases in the final product.  Fewer folds, cleaner results.

- **Eyeballing is OK**
    
    - For the regular polygonal faces I have tried to give exact folds (e.g. - fold this corner to this point), but as I have moved to things like the Catalan solids, I have relaxed this to accommodate more arbitrary angles.
    
- **Over-engineering is OK**

    - After all these statements that nothing is exact, I still want to design models that are as close to the exact result as possible.  This contradiction allows me to both fixate on small details and to move on when I have a result that is "good enough".

## Contents

- `polyhedra.pdf` Instructions on folding units for polyhedra with regular polygonal faces - i.e. Platonic, Archimedean, and Johnson solids.

- `fold_app.py` Code for a Streamlit app to generate instructions for both defined polyhedra and arbitrary units.

- `latex` Folder containing the $\LaTeX$ script to generate `polyhedra.pdf`

- `figs` Folder containing Gnuplot scripts to generate the figures in `polyhedra.pdf`.  These are done "by hand" and are not well documented.

- `catalan` Folder containing undocumented code/scripts I have generated to explore the angles and edge lengths of the Catalan solids.  Ultimately, `catalan.c` will be the only relevant code, the others being redundant/irrelevant.

- `gallery` Collection of photos of models I have folded using these units.


## Future tasks / known shortcomings

- `polyhedra.pdf` needs work.  A consistent formatting of image sizes needs to be implemented.  There are no directions of how to join units.  Notes should be added to clarify some aspects.  Like how tearing the tab in for the triangle faces is necessary for Platonic solids as opposed to Archimedean solids.  Also forewarn the reader that the snub polyhedra require more patience to assemble.

- `catalan` needs to be documented and cleaned.

- `gallery` needs more pictures!  Group by family and individual.

- Most work will focus on `fold_app.py`.
    - Add a boolean to remove the bottom tab.
    - Link various units needed for a given polyhedra.
    - Work on writing the fold description for the step that creates the angle.
    - Add units for all Platonic, Archimedean, and Catalan solids to presets.
    - Allow for variable paper sizes, not only the half letter paper proportion I use.
    - Some small angles will create folds that extend over the top left corner and some large angles will extend over the bottom right corner.  The diagrams are jumbled and unphysical in these circumastances.  Beyond saying that it's a good idea to avoid this, perhaps catch it in the code and prevent the horrible diagrams.
