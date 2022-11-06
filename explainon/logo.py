import manim as mnm

SCALAR_BOSONS = dict(higgs="H")

GAUGE_BOSONS = dict(
    gluon="g", 
    photon="\\gamma", 
    z_boson="Z",
    w_boson="W",
)

QUARKS = dict(
    up="u",
    down="d",
    charm="c",
    strange="s",
    top="t",
    bottom="b",
)

LEPTONS = dict(
    electron="e",
    muon="\\mu",
    tau="\\tau",
    electron_neutrino="\\nu_e",
    muon_neutrino="\\nu_{\\mu}",
    tau_neutrino="\\nu_{\\tau}",
)

CUSTOM = dict(explainon="\\epsilon")

LOGO_COLOR = dict(
    scalar_bosons=mnm.YELLOW,
    gauge_bosons=mnm.RED,
    quarks=mnm.PURPLE,
    leptons=mnm.GREEN,
    custom=mnm.BLUE,
)

ALL_PARTICLES = {
    **SCALAR_BOSONS, 
    **GAUGE_BOSONS, 
    **QUARKS, 
    **LEPTONS,
    **CUSTOM,
}

PARTICLES_TO_GROUP = dict({
    *list(zip(SCALAR_BOSONS.keys(), ("scalar_bosons",)*len(SCALAR_BOSONS))),
    *list(zip(GAUGE_BOSONS.keys(), ("gauge_bosons",)*len(GAUGE_BOSONS))),
    *list(zip(QUARKS.keys(), ("quarks",)*len(QUARKS))),
    *list(zip(LEPTONS.keys(), ("leptons",)*len(LEPTONS))),
    *list(zip(CUSTOM.keys(), ("custom",)*len(CUSTOM))),
})

def create_particle_logo(
    label=r"\epsilon", 
    radius=0.55, 
    color=mnm.color_gradient((mnm.WHITE, mnm.BLUE), 10),
    font_color=mnm.BLACK, 
    font_size=75
):
    particle_logo = mnm.MathTex(
        label, 
        color=font_color, 
        font_size=font_size
    )
    
    particle_logo = mnm.LabeledDot(
        label=particle_logo, 
        radius=radius, 
        fill_color=color
    )
    
    return particle_logo

PARTICLE_LOGO = {
    k: create_particle_logo(
        label=v, 
        color=mnm.color_gradient(
            (mnm.WHITE, LOGO_COLOR[PARTICLES_TO_GROUP[k]]), 10
        )
    )
    for k, v in ALL_PARTICLES.items()
}