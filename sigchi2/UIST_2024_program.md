
## Manipulating Text
### Beyond the Chat: Executable and Verifiable Text-Editing with LLMs
Authors: Philippe Laban, Jesse Vig, Marti Hearst, Caiming Xiong, Chien-Sheng Wu

[Link](https://programs.sigchi.org/uist/2024/program/content/170790)

Abstract: Conversational interfaces powered by Large Language Models (LLMs) have recently become a popular way to obtain feedback during document editing. However, standard chat-based conversational interfaces cannot explicitly surface the editing changes that they suggest. To give the author more control when editing with an LLM, we present InkSync, an editing interface that suggests executable edits directly within the document being edited. Because LLMs are known to introduce factual errors, Inksync also supports a 3-stage approach to mitigate this risk: Warn authors when a suggested edit introduces new information, help authors Verify the new information's accuracy through external search, and allow a third party to Audit with a-posteriori verification via a trace of all auto-generated content.
Two usability studies confirm the effectiveness of InkSync's components when compared to standard LLM-based chat interfaces, leading to more accurate and more efficient editing, and improved user experience.



### ScriptViz: A Visualization Tool to Aid Scriptwriting based on a Large Movie Database
Authors: Anyi Rao, Jean-Peïc Chou, Maneesh Agrawala

[Link](https://programs.sigchi.org/uist/2024/program/content/170838)

Abstract: Scriptwriters usually rely on their mental visualization to create a vivid story by using their imagination to see, feel, and experience the scenes they are writing. Besides mental visualization, they often refer to existing images or scenes in movies and analyze the visual elements to create a certain mood or atmosphere. In this paper, we develop a new tool, ScriptViz, to provide external visualization based on a large movie database for the screenwriting process. It retrieves reference visuals on the fly based on scripts’ text and dialogue from a large movie database. The tool provides two types of control on visual elements that enable writers to 1) see exactly what they want with fixed visual elements and 2) see variances in uncertain elements. User evaluation among 15 scriptwriters shows that ScriptViz is able to present scriptwriters with consistent yet diverse visual possibilities, aligning closely with their scripts and helping their creation.




### SkipWriter: LLM-Powered Abbreviated Writing on Tablets
Authors: Zheer Xu, Shanqing Cai, Mukund Varma T, Subhashini Venugopalan, Shumin Zhai

[Link](https://programs.sigchi.org/uist/2024/program/content/170930)

Abstract: Large Language Models (LLMs) may offer transformative opportunities for text input, especially for physically demanding modalities like handwriting. We studied a form of abbreviated handwriting by designing, developing, and evaluating a prototype, named SkipWriter, that converts handwritten strokes of a variable-length prefix-based abbreviation (e.g. "ho a y" as handwritten strokes) into the intended full phrase (e.g., "how are you" in the digital format) based on the preceding context. SkipWriter consists of an in-production handwriting recognizer and an LLM fine-tuned on this task. With flexible pen input, SkipWriter allows the user to add and revise prefix strokes when predictions do not match the user's intent. An user evaluation demonstrated a 60% reduction in motor movements with an average speed of 25.78 WPM. We also showed that this reduction is close to the ceiling of our model in an offline simulation.



### Bluefish: Composing Diagrams with Declarative Relations
Authors: Josh Pollock, Catherine Mei, Grace Huang, Elliot Evans, Daniel Jackson, Arvind Satyanarayan

[Link](https://programs.sigchi.org/uist/2024/program/content/170824)

Abstract: Diagrams are essential tools for problem-solving and communication as they externalize conceptual structures using spatial relationships. But when picking a diagramming framework, users are faced with a dilemma. They can either use a highly expressive but low-level toolkit, whose API does not match their domain-specific concepts, or select a high-level typology, which offers a recognizable vocabulary but supports a limited range of diagrams. To address this gap, we introduce Bluefish: a diagramming framework inspired by component-based user interface (UI) libraries. Bluefish lets users create diagrams using relations: declarative, composable, and extensible diagram fragments that relax the concept of a UI component. Unlike a component, a relation does not have sole ownership over its children nor does it need to fully specify their layout. To render diagrams, Bluefish extends a traditional tree-based scenegraph to a compound graph that captures both hierarchical and adjacent relationships between nodes. To evaluate our system, we construct a diverse example gallery covering many domains including mathematics, physics, computer science, and even cooking. We show that Bluefish's relations are effective declarative primitives for diagrams. Bluefish is open source, and we aim to shape it into both a usable tool and a research platform.




## Future Fabrics
### ScrapMap: Interactive Color Layout for Scrap Quilting
Authors: Mackenzie Leake, Ross Daly

[Link](https://programs.sigchi.org/uist/2024/program/content/170743)

Abstract: Scrap quilting is a popular sewing process that involves combining leftover pieces of fabric into traditional patchwork designs. Imagining the possibilities for these leftovers and arranging the fabrics in such a way that achieves visual goals, such as high contrast, can be challenging given the large number of potential fabric assignments within the quilt's design. We formulate the task of designing a scrap quilt as a graph coloring problem with domain-specific coloring and material constraints. Our interactive tool called ScrapMap helps quilters explore these potential designs given their available materials by leveraging the hierarchy of scrap quilt construction (e.g., quilt blocks and motifs) and providing user-directed automatic block coloring suggestions. Our user evaluation indicates that quilters find ScrapMap useful for helping them consider new ways to use their scraps and create visually striking quilts.



### What's in a cable? Abstracting Knitting Design Elements with Blended Raster/Vector Primitives
Authors: Hannah Twigg-Smith, Yuecheng Peng, Emily Whiting, Nadya Peek

[Link](https://programs.sigchi.org/uist/2024/program/content/170811)

Abstract: In chart-based programming environments for machine knitting, patterns are specified at a low level by placing operations on a grid. This highly manual workflow makes it challenging to iterate on design elements such as cables, colorwork, and texture. While vector-based abstractions for knitting design elements may facilitate higher-level manipulation, they often include interdependencies which require stitch-level reconciliation. To address this, we contribute a new way of specifying knits with blended vector and raster primitives. Our abstraction supports the design of interdependent elements like colorwork and texture. We have implemented our blended raster/vector specification in a direct manipulation design tool where primitives are layered and rasterized, allowing for simulation of the resulting knit structure and generation of machine instructions. Through examples, we show how our approach enables higher-level manipulation of various knitting techniques, including intarsia colorwork, short rows, and cables. Specifically, we show how our tool supports the design of complex patterns including origami pleat patterns and capacitive sensor patches.



### Embrogami: Shape-Changing Textiles with Machine Embroidery
Authors: Yu Jiang, Alice Haynes, Narjes Pourjafarian, Jan Borchers, Jürgen Steimle

[Link](https://programs.sigchi.org/uist/2024/program/content/170971)

Abstract: Machine embroidery is a versatile technique for creating custom and entirely fabric-based patterns on thin and conformable textile surfaces. However, existing machine-embroidered surfaces remain static, limiting the interactions they can support. We introduce Embrogami, an approach for fabricating textile structures with versatile shape-changing behaviors. Inspired by origami, we leverage machine embroidery to form finger-tip-scale mountain-and-valley structures on textiles with customized shapes, bistable or elastic behaviors, and modular composition. The structures can be actuated by the user or the system to modify the local textile surface topology, creating interactive elements like toggles and sliders or textile shape displays with an ultra-thin, flexible, and integrated form factor. We provide a dedicated software tool and report results of technical experiments to allow users to flexibly design, fabricate, and deploy customized Embrogami structures. With four application cases, we showcase Embrogami’s potential to create functional and flexible shape-changing textiles with diverse visuo-tactile feedback.



### KODA: Knit-program Optimization by Dependency Analysis
Authors: Megan Hofmann

[Link](https://programs.sigchi.org/uist/2024/program/content/170935)

Abstract: Digital knitting machines have the capability to reliably manufacture seamless, textured, and multi-material garments, but these capabilities are obscured by limiting CAD tools. Recent innovations in computational knitting build on emerging programming infrastructure that gives full access to the machine's capabilities but requires an extensive understanding of machine operations and execution.  In this paper, we contribute a critical missing piece of the knitting-machine programming pipeline--a program optimizer. Program optimization allows programmers to focus on developing novel algorithms that produce desired fabrics while deferring concerns of efficient machine operations to the optimizer. We present KODA, the Knit-program Optimization by Dependency Analysis method. KODA re-orders and reduces machine instructions to reduce knitting time, increase knitting reliability, and manage boilerplate operations that adjust the machine state. The result is a system that enables programmers to write readable and intuitive knitting algorithms while producing efficient and verified programs. 



### X-Hair: 3D Printing Hair-like Structures with Multi-form, Multi-property and Multi-function
Authors: Guanyun Wang, Junzhe Ji, Yunkai Xu, Lei Ren, Xiaoyang Wu, Chunyuan Zheng, Xiaojing Zhou, Xin Tang, Boyu Feng, Lingyun Sun, Ye Tao, Jiaji Li

[Link](https://programs.sigchi.org/uist/2024/program/content/171007)

Abstract: In this paper, we present X-Hair, a method that enables 3D-printed hair with various forms, properties, and functions. We developed a two-step suspend printing strategy to fabricate hair-like structures in different forms (e.g. fluff, bristle, barb) by adjusting parameters including Extrusion Length Ratio and Total Length. Moreover, a design tool is also established for users to customize hair-like structures with various properties (e.g. pointy, stiff, soft) on imported 3D models, which virtually shows the results for previewing and generates G-code files for 3D printing. We demonstrate the design space of X-Hair and evaluate the properties of them with different parameters. Through a series of applications with hair-like structures, we validate X-hair's practical usage of biomimicry, decoration, heat preservation, adhesion, and haptic interaction.



### TouchpadAnyWear: Textile-Integrated Tactile Sensors for Multimodal High Spatial-Resolution Touch Inputs with Motion Artifacts Tolerance
Authors: Junyi Zhao, Pornthep Preechayasomboon, Tyler Christensen, Amirhossein H. Memar, Zhenzhen Shen, Nick Colonnese, Michael Khbeis, Mengjia Zhu

[Link](https://programs.sigchi.org/uist/2024/program/content/170873)

Abstract: This paper presents TouchpadAnyWear, a novel family of textile-integrated force sensors capable of multi-modal touch input, encompassing micro-gesture detection, two-dimensional (2D) continuous input, and force-sensitive strokes. This thin (\textless 1.5~mm) and conformal device features high spatial resolution sensing and motion artifact tolerance through its unique capacitive sensor architecture. The sensor consists of a knitted textile compressive core, sandwiched by stretchable silver electrodes, and conductive textile shielding layers on both sides. With a high-density sensor pixel array (25/cm\textsuperscript{2}), TouchpadAnyWear can detect touch input locations and sizes with millimeter-scale spatial resolution and a wide range of force inputs (0.05~N to 20~N). The incorporation of miniature polymer domes, referred to as ``poly-islands'', onto the knitted textile locally stiffens the sensing areas, thereby reducing motion artifacts during deformation. These poly-islands also provide passive tactile feedback to users, allowing for eyes-free localization of the active sensing pixels. Design choices and sensor performance are evaluated using in-depth mechanical characterization. Demonstrations include an 8-by-8 grid sensor as a miniature high-resolution touchpad and a T-shaped sensor for thumb-to-finger micro-gesture input. User evaluations validate the effectiveness and usability of TouchpadAnyWear in daily interaction contexts, such as tapping, forceful pressing, swiping, 2D cursor control, and 2D stroke-based gestures. This paper further discusses potential applications and explorations for TouchpadAnyWear in wearable smart devices, gaming, and augmented reality devices.




## Storytime
### Story-Driven: Exploring the Impact of Providing Real-time Context Information on Automated Storytelling
Authors: Jan Henry Belz, Lina Weilke, Anton Winter, Philipp Hallgarten, Enrico Rukzio, Tobias Grosse-Puppendahl

[Link](https://programs.sigchi.org/uist/2024/program/content/170763)

Abstract: Stories have long captivated the human imagination with narratives that enrich our lives. Traditional storytelling methods are often static and not designed to adapt to the listener’s environment, which is full of dynamic changes. For instance, people often listen to stories in the form of podcasts or audiobooks while traveling in a car. Yet, conventional in-car storytelling systems do not embrace the adaptive potential of this space. The advent of generative AI is the key to creating content that is not just personalized but also responsive to the changing parameters of the environment. We introduce a novel system for interactive, real-time story narration that leverages environment and user context in correspondence with estimated arrival times to adjust the generated story continuously. Through two comprehensive real-world studies with a total of 30 participants in a vehicle, we assess the user experience, level of immersion, and perception of the environment provided by the prototype. Participants' feedback shows a significant improvement over traditional storytelling and highlights the importance of context information for generative storytelling systems. 



### Lumina: A Software Tool for Fostering Creativity in Designing Chinese Shadow Puppets
Authors: Zhihao Yao, Yao Lu, Qirui Sun, Shiqing Lyu, Hanxuan Li, Xing-Dong Yang, Xuezhu Wang, Guanhong Liu, Haipeng Mi

[Link](https://programs.sigchi.org/uist/2024/program/content/170765)

Abstract: Shadow puppetry, a culturally rich storytelling art, faces challenges transitioning to the digital realm. Creators in the early design phase struggle with crafting intricate patterns, textures, and basic animations while adhering to stylistic conventions - hindering creativity, especially for novices. This paper presents Lumina, a tool to facilitate the early Chinese shadow puppet design stage. Lumina provides contour templates, animations, scene editing tools, and machine-generated traditional puppet patterns. These features liberate creators from tedious tasks, allowing focus on the creative process. Developed based on a formative study with puppet creators, the web-based Lumina enables wide dissemination. An evaluation with 18 participants demonstrated Lumina's effectiveness and ease of use, with participants successfully creating designs spanning traditional themes to contemporary and science-fiction concepts.



### PortalInk: 2.5D Visual Storytelling with SVG Parallax and Waypoint Transitions
Authors: Tongyu Zhou, Joshua Yang, Vivian Chan, Ji Won Chung, Jeff Huang

[Link](https://programs.sigchi.org/uist/2024/program/content/170783)

Abstract: Efforts to expand the authoring of visual stories beyond the 2D canvas have commonly mapped flat imagery to 3D scenes or objects. This translation requires spatial reasoning, as artists must think in two spaces. We propose PortalInk, a tool for artists to craft and export 2.5D graphical stories while remaining in 2D space by using SVG transitions. This is achieved via a parallax effect that generates a sense of depth that can be further explored using pan and zoom interactions. Any canvas position can be saved and linked to in a closed drawn stroke, or "portal," allowing the artist to create spatially discontinuous, or even infinitely looping visual trajectories. We provide three case studies and a gallery to demonstrate how artists can naturally incorporate these interactions to craft immersive comics, as well as re-purpose them to support use cases beyond drawing such as animation, slide-based presentations, web design, and digital journalism.



### DrawTalking: Building Interactive Worlds by Sketching and Speaking
Authors: Karl Rosenberg, Rubaiat Habib Kazi, Li-Yi Wei, Haijun Xia, Ken Perlin

[Link](https://programs.sigchi.org/uist/2024/program/content/170730)

Abstract: We introduce DrawTalking, an approach to building and controlling interactive worlds by sketching and speaking while telling stories. It emphasizes user control and flexibility, and gives programming-like capability without requiring code. An early open-ended study with our prototype shows that the mechanics resonate and are applicable to many creative-exploratory use cases, with the potential to inspire and inform research in future natural interfaces for creative exploration and authoring.



### Patchview: LLM-powered Worldbuilding with Generative Dust and Magnet Visualization
Authors: John Chung, Max Kreminski

[Link](https://programs.sigchi.org/uist/2024/program/content/170729)

Abstract: Large language models (LLMs) can help writers build story worlds by generating world elements, such as factions, characters, and locations. However, making sense of many generated elements can be overwhelming. Moreover, if the user wants to precisely control aspects of generated elements that are difficult to specify verbally, prompting alone may be insufficient. We introduce Patchview, a customizable LLM-powered system that visually aids worldbuilding by allowing users to interact with story concepts and elements through the physical metaphor of magnets and dust. Elements in Patchview are visually dragged closer to concepts with high relevance, facilitating sensemaking. The user can also steer the generation with verbally elusive concepts by indicating the desired position of the element between concepts. When the user disagrees with the LLM's visualization and generation, they can correct those by repositioning the element. These corrections can be used to align the LLM's future behaviors to the user's perception. With a user study, we show that Patchview supports the sensemaking of world elements and steering of element generation, facilitating exploration during the worldbuilding process. Patchview provides insights on how customizable visual representation can help sensemake, steer, and align generative AI model behaviors with the user's intentions.



### An Interactive System for Suporting Creative Exploration of Cinematic Composition Designs
Authors: Rui He, Huaxin Wei, Ying Cao

[Link](https://programs.sigchi.org/uist/2024/program/content/170806)

Abstract: Designing cinematic compositions, which involves moving cameras through a scene, is essential yet challenging in filmmaking. Machinima filmmaking provides real-time virtual environments for exploring different compositions flexibly and efficiently. However, producing high-quality cinematic compositions in such environments still requires significant cinematography skills and creativity. This paper presents Cinemassist, a tool designed to support and enhance this creative process by generating a variety of cinematic composition proposals at both keyframe and scene levels, which users can incorporate into their workflows and achieve more creative results. At the crux of our system is a deep generative model trained on real movie data, which can generate plausible, diverse camera poses conditioned on 3D animations and additional input semantics. Our model enables an interactive cinematic composition design workflow where users can co-design with the model by being inspired by model-generated suggestions while having control over the generation process. Our user study and expert rating find Cinemassist can facilitate the design process for users of different backgrounds and enhance the design quality especially for users with animation expertise, demonstrating its potential as an invaluable tool in the context of digital filmmaking.




## Beyond mobile
### picoRing: battery-free rings for subtle thumb-to-index input
Authors: Ryo Takahashi, Eric Whitmire, Roger Boldu, Shiu Ng, Wolf Kienzle, Hrvoje Benko

[Link](https://programs.sigchi.org/uist/2024/program/content/170844)

Abstract: Smart rings for subtle, reliable finger input offer an attractive path for ubiquitous interaction with wearable computing platforms. 
However, compared to ordinary rings worn for cultural or fashion reasons, smart rings are much bulkier and less comfortable, largely due to the space required for a battery, which also limits the space available for sensors.
This paper presents picoRing, a flexible sensing architecture that enables a variety of battery-free smart rings paired with a wristband. 
By inductively connecting a wristband-based sensitive reader coil with a ring-based fully-passive sensor coil, picoRing enables the wristband to stably detect the passive response from the ring via a weak inductive coupling. 
We demonstrate four different rings that support thumb-to-finger interactions like pressing, sliding, or scrolling.
When users perform these interactions, the corresponding ring converts each input into a unique passive response through a network of passive switches.
Combining the coil-based sensitive readout with the fully-passive ring design enables a tiny ring that weighs as little as 1.5 g and achieves a 13 cm stable readout despite finger bending, and proximity to metal.



### WatchLink: Enhancing Smartwatches with Sensor Add-Ons via ECG Interface
Authors: Anandghan Waghmare, Ishan Chatterjee, Vikram Iyer, Shwetak Patel

[Link](https://programs.sigchi.org/uist/2024/program/content/170782)

Abstract: We introduce a low-power communication method that lets smartwatches leverage existing electrocardiogram (ECG) hardware as a data communication interface.  Our unique approach enables the connection of external, inexpensive, and low-power "add-on" sensors to the smartwatch, expanding its functionalities. These sensors cater to specialized user needs beyond those offered by pre-built sensor suites, at a fraction of the cost and power of traditional communication protocols, including Bluetooth Low Energy. To demonstrate the feasibility of our approach, we conduct a series of exploratory and evaluative tests to characterize the ECG interface as a communication channel on commercial smartwatches. We design a simple transmission scheme using commodity components, demonstrating cost and power benefits. Further, we build and test a suite of add-on sensors, including UV light, body temperature, buttons, and breath alcohol, all of which achieved testing objectives at low material cost and power usage. This research paves the way for personalized and user-centric wearables by offering a cost-effective solution to expand their functionalities.




### PrISM-Observer: Intervention Agent to Help Users Perform Everyday Procedures Sensed using a Smartwatch
Authors: Riku Arakawa, Hiromu Yakura, Mayank Goel

[Link](https://programs.sigchi.org/uist/2024/program/content/170914)

Abstract: We routinely perform procedures (such as cooking) that include a set of atomic steps. Often, inadvertent omission or misordering of a single step can lead to serious consequences, especially for those experiencing cognitive challenges such as dementia. This paper introduces PrISM-Observer, a smartwatch-based, context-aware, real-time intervention system designed to support daily tasks by preventing errors. Unlike traditional systems that require users to seek out information, the agent observes user actions and intervenes proactively. This capability is enabled by the agent's ability to continuously update its belief in the user's behavior in real-time through multimodal sensing and forecast optimal intervention moments and methods. We first validated the steps-tracking performance of our framework through evaluations across three datasets with different complexities. Then, we implemented a real-time agent system using a smartwatch and conducted a user study in a cooking task scenario. The system generated helpful interventions, and we gained positive feedback from the participants. The general applicability of PrISM-Observer to daily tasks promises broad applications, for instance, including support for users requiring more involved interventions, such as people with dementia or post-surgical patients.




## Validation in AI/ML
### Natural Expression of a Machine Learning Model's Uncertainty Through Verbal and Non-Verbal Behavior of Intelligent Virtual Agents
Authors: Susanne Schmidt, Tim Rolff, Henrik Voigt, Micha Offe, Frank Steinicke

[Link](https://programs.sigchi.org/uist/2024/program/content/170826)

Abstract: Uncertainty cues are inherent in natural human interaction, as they signal to communication partners how much they can rely on conveyed information. Humans subconsciously provide such signals both verbally (e.g., through expressions such as "maybe" or "I think") and non-verbally (e.g., by diverting their gaze). In contrast, artificial intelligence (AI)-based services and machine learning (ML) models such as ChatGPT usually do not disclose the reliability of answers to their users.
In this paper, we explore the potential of combining ML models as powerful information sources with human means of expressing uncertainty to contextualize the information. We present a comprehensive pipeline that comprises (1) the human-centered collection of (non-)verbal uncertainty cues, (2) the transfer of cues to virtual agent videos, (3) the annotation of videos for perceived uncertainty, and (4) the subsequent training of a custom ML model that can generate uncertainty cues in virtual agent behavior. In a final step (5), the trained ML model is evaluated in terms of both fidelity and generalizability of the generated (non-)verbal uncertainty behavior.



### Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
Authors: Shreya Shankar, J.D. Zamfirescu-Pereira, Bjoern Hartmann, Aditya Parameswaran, Ian Arawjo

[Link](https://programs.sigchi.org/uist/2024/program/content/170954)

Abstract: Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs. Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation. We present a mixed-initiative approach to “validate the validators”— aligning LLM-generated evaluation functions (be it prompts or code) with human requirements. Our interface, EvalGen, provides automated assistance to users in generating evaluation criteria and implementing assertions. While generating candidate implementations (Python functions, LLM grader prompts), EvalGen asks humans to grade a subset of LLM outputs; this feedback is used to select implementations that better align with user grades. A qualitative study finds overall support for EvalGen but underscores the subjectivity and iterative nature of alignment. In particular, we identify a phenomenon we dub criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appear dependent on the specific LLM outputs observed (rather than independent and definable a priori), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs. We present our interface and implementation details, a comparison of our algorithm with a baseline approach, and implications for the design of future LLM evaluation assistants.



### LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation
Authors: Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu

[Link](https://programs.sigchi.org/uist/2024/program/content/170831)

Abstract: The emergent large language/multimodal models facilitate the evolution of mobile agents, especially in mobile UI task automation. However, existing evaluation approaches, which rely on human validation or established datasets to compare agent-predicted actions with predefined action sequences, are unscalable and unfaithful. To overcome these limitations, this paper presents LlamaTouch, a testbed for on-device mobile UI task execution and faithful, scalable task evaluation. By observing that the task execution process only transfers UI states, LlamaTouch employs a novel evaluation approach that only assesses whether an agent traverses all manually annotated, essential application/system states. LlamaTouch comprises three key techniques: (1) On-device task execution that enables mobile agents to interact with realistic mobile environments for task execution. (2) Fine-grained UI component annotation that merges pixel-level screenshots and textual screen hierarchies to explicitly identify and precisely annotate essential UI components with a rich set of designed annotation primitives. (3) A multi-level application state matching algorithm that utilizes exact and fuzzy matching to accurately detect critical information in each screen, even with unpredictable UI layout/content dynamics. LlamaTouch currently incorporates four mobile agents and 496 tasks, encompassing both tasks in the widely-used datasets and our self-constructed ones to cover more diverse mobile applications. Evaluation results demonstrate LlamaTouch’s high faithfulness of evaluation in real-world mobile environments and its better scalability than human validation. LlamaTouch also enables easy task annotation and integration of new mobile agents. Code and dataset are publicly available at https://github.com/LlamaTouch/LlamaTouch.



### Clarify: Improving Model Robustness With Natural Language Corrections
Authors: Yoonho Lee, Michelle Lam, Helena Vasconcelos, Michael Bernstein, Chelsea Finn

[Link](https://programs.sigchi.org/uist/2024/program/content/170784)

Abstract: The standard way to teach models is by feeding them lots of data. However, this approach often teaches models incorrect ideas because they pick up on misleading signals in the data. To prevent such misconceptions, we must necessarily provide additional information beyond the training data.  Prior methods incorporate additional instance-level supervision, such as labels for misleading features or additional labels for debiased data.  However, such strategies require a large amount of labeler effort. We hypothesize that people are good at providing textual feedback at the concept level, a capability that existing teaching frameworks do not leverage. We propose Clarify, a novel interface and method for interactively correcting model misconceptions. Through Clarify, users need only provide a short text description of a model's consistent failure patterns. Then, in an entirely automated way, we use such descriptions to improve the training process. Clarify is the first end-to-end system for user model correction. Our user studies show that non-expert users can successfully describe model misconceptions via Clarify, leading to increased worst-case performance in two datasets. We additionally conduct a case study on a large-scale image dataset, ImageNet, using Clarify to find and rectify 31 novel hard subpopulations.



### "The Data Says Otherwise" – Towards Automated Fact-checking and Communication of Data Claims
Authors: Yu Fu, Shunan Guo, Jane Hoffswell, Victor S. Bursztyn, Ryan Rossi, John Stasko

[Link](https://programs.sigchi.org/uist/2024/program/content/170762)

Abstract: Fact-checking data claims requires data evidence retrieval and analysis, which can become tedious and intractable when done manually. This work presents Aletheia, an automated fact-checking prototype designed to facilitate data claims verification and enhance data evidence communication. For verification, we utilize a pre-trained LLM to parse the semantics for evidence retrieval. To effectively communicate the data evidence, we design representations in two forms: data tables and visualizations, tailored to various data fact types. Additionally, we design interactions that showcase a real-world application of these techniques. We evaluate the performance of two core NLP tasks with a curated dataset comprising 400 data claims and compare the two representation forms regarding viewers’ assessment time, confidence, and preference via a user study with 20 participants. The evaluation offers insights into the feasibility and bottlenecks of using LLMs for data fact-checking tasks, potential advantages and disadvantages of using visualizations over data tables, and design recommendations for presenting data evidence.




## A11y
### ProgramAlly: Creating Custom Visual Access Programs via Multi-Modal End-User Programming
Authors: Jaylin Herskovitz, Andi Xu, Rahaf Alharbi, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170960)

Abstract: Existing visual assistive technologies are built for simple and common use cases, and have few avenues for blind people to customize their functionalities. Drawing from prior work on DIY assistive technology, this paper investigates end-user programming as a means for users to create and customize visual access programs to meet their unique needs. We introduce ProgramAlly, a system for creating custom filters for visual information, e.g., 'find NUMBER on BUS', leveraging three end-user programming approaches: block programming, natural language, and programming by example. To implement ProgramAlly, we designed a representation of visual filtering tasks based on scenarios encountered by blind people, and integrated a set of on-device and cloud models for generating and running these programs. In user studies with 12 blind adults, we found that participants preferred different programming modalities depending on the task, and envisioned using visual access programs to address unique accessibility challenges that are otherwise difficult with existing applications. Through ProgramAlly, we present an exploration of how blind end-users can create visual access programs to customize and control their experiences.



### Accessible Gesture Typing on Smartphones for People with Low Vision
Authors: Dan Zhang, Zhi Li, Vikas Ashok, William H Seiple, IV Ramakrishnan, Xiaojun Bi

[Link](https://programs.sigchi.org/uist/2024/program/content/170887)

Abstract: While gesture typing is widely adopted on touchscreen keyboards, its support for low vision users is limited.  We have designed and implemented two keyboard prototypes, layout-magnified and key-magnified keyboards, to enable gesture typing for people with low vision. Both keyboards facilitate uninterrupted access to all keys while the screen magnifier is active, allowing people with low vision to input text with one continuous stroke. Furthermore, we have created a kinematics-based decoding algorithm to accommodate the typing behavior of people with low vision. This algorithm can decode the gesture input even if the gesture trace deviates from a pre-defined word template, and the starting position of the gesture is far from the starting letter of the target word. Our user study showed that the key-magnified keyboard achieved 5.28 words per minute, 27.5% faster than a conventional gesture typing keyboard with voice feedback.



### AccessTeleopKit: A Toolkit for Creating Accessible Web-Based Interfaces for Tele-Operating an Assistive Robot
Authors: Vinitha Ranganeni, Varad Dhat, Noah Ponto, Maya Cakmak

[Link](https://programs.sigchi.org/uist/2024/program/content/170825)

Abstract: Mobile manipulator robots, which can move around and physically interact with their environments, can empower people with motor limitations to independently carry out many activities of daily living. While many interfaces have been developed for tele-operating complex robots, most of them are not accessible to people with severe motor limitations. Further, most interfaces are rigid with limited configurations and are not readily available to download and use. To address these barriers, we developed AccessTeleopKit: an open-source toolkit for creating custom and accessible robot tele-operation interfaces based on cursor-and-click input for the Stretch 3 mobile-manipulator. With AccessTeleopKit users can add, remove, and rearrange components such as buttons and camera views, and select between a variety of control modes. We describe the participatory and iterative design process that led to the current implementation of AccessTeleopKit, involving three long-term deployments of the robot in the home of a quadriplegic user. We demonstrate how AccessTeleopKit allowed the user to create different interfaces for different tasks and the diversity of tasks it allowed the user to carry out. We also present two studies involving six additional users with severe motor limitations, demonstrating the power of AccessTeleopKit in creating custom interfaces for different user needs and preferences.



### Memory Reviver: Supporting Photo-Collection Reminiscence for People with Visual Impairment via a Proactive Chatbot
Authors: Shuchang Xu, Chang Chen, Zichen LIU, Xiaofu Jin, Linping Yuan, Yukang Yan, Huamin Qu

[Link](https://programs.sigchi.org/uist/2024/program/content/170852)

Abstract: Reminiscing with photo collections offers significant psychological benefits but poses challenges for people with visual impairment (PVI). Their current reliance on sighted help restricts the flexibility of this activity. In response, we explored using a chatbot in a preliminary study. We identified two primary challenges that hinder effective reminiscence with a chatbot: the scattering of information and a lack of proactive guidance. To address these limitations, we present Memory Reviver, a proactive chatbot that helps PVI reminisce with a photo collection through natural language communication. Memory Reviver incorporates two novel features: (1) a Memory Tree, which uses a hierarchical structure to organize the information in a photo collection; and (2) a Proactive Strategy, which actively delivers information to users at proper conversation rounds. Evaluation with twelve PVI demonstrated that Memory Reviver effectively facilitated engaging reminiscence, enhanced understanding of photo collections, and delivered natural conversational experiences. Based on our findings, we distill implications for supporting photo reminiscence and designing chatbots for PVI.



### VizAbility: Enhancing Chart Accessibility with LLM-based Conversational Interaction
Authors: Joshua Gorniak, Yoon Kim, Donglai Wei, Nam Wook Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/171009)

Abstract: Traditional accessibility methods like alternative text and data tables typically underrepresent data visualization's full potential. Keyboard-based chart navigation has emerged as a potential solution, yet efficient data exploration remains challenging. We present VizAbility, a novel system that enriches chart content navigation with conversational interaction, enabling users to use natural language for querying visual data trends. VizAbility adapts to the user's navigation context for improved response accuracy and facilitates verbal command-based chart navigation. Furthermore, it can address queries for contextual information, designed to address the needs of visually impaired users. We designed a large language model (LLM)-based pipeline to address these user queries, leveraging chart data & encoding, user context, and external web knowledge. We conducted both qualitative and quantitative studies to evaluate VizAbility's multimodal approach. We discuss further opportunities based on the results, including improved benchmark testing, incorporation of vision models, and integration with visualization workflows.



### Computational Trichromacy Reconstruction: Empowering the Color-Vision Deficient to Recognize Colors Using Augmented Reality
Authors: Yuhao Zhu, Ethan Chen, Colin Hascup, Yukang Yan, Gaurav Sharma

[Link](https://programs.sigchi.org/uist/2024/program/content/170991)

Abstract: We propose an assistive technology that helps individuals with Color Vision Deficiencies (CVD) to recognize/name colors.
A dichromat's color perception is a reduced two-dimensional (2D) subset of a normal
trichromat's three dimensional color (3D) perception, leading to confusion when visual stimuli that appear identical to the dichromat are referred to by different color names.
Using our proposed system, CVD individuals can interactively induce distinct perceptual changes to originally confusing colors via a computational color space transformation.
By combining their original 2D precepts for colors with the discriminative changes, a three dimensional color space is reconstructed, where the dichromat can learn to resolve color name confusions and accurately recognize colors.
Our system is implemented as an Augmented Reality (AR) interface on smartphones, where users interactively control the rotation through swipe gestures and observe the induced color shifts in the camera view or in a displayed image. Through psychophysical experiments and a longitudinal user study, we demonstrate that such rotational color shifts have discriminative power (initially confusing colors become distinct under rotation) and exhibit structured perceptual shifts dichromats can learn with modest training. The AR App is also evaluated in two real-world scenarios (building with lego blocks and interpreting artistic works); users all report positive experience in using the App to recognize object colors that they otherwise could not.




## Contextual Augmentations
### StreetNav: Leveraging Street Cameras to Support Precise Outdoor Navigation for Blind Pedestrians
Authors: Gaurav Jain, Basel Hindi, Zihao Zhang, Koushik Srinivasula, Mingyu Xie, Mahshid Ghasemi, Daniel Weiner, Sophie Ana Paris, Xin Yi Therese Xu, Michael Malcolm, Mehmet Kerem Turkcan, Javad Ghaderi, Zoran Kostic, Gil Zussman, Brian Smith

[Link](https://programs.sigchi.org/uist/2024/program/content/171003)

Abstract: Blind and low-vision (BLV) people rely on GPS-based systems for outdoor navigation. GPS's inaccuracy, however, causes them to veer off track, run into obstacles, and struggle to reach precise destinations. While prior work has made precise navigation possible indoors via hardware installations, enabling this outdoors remains a challenge. Interestingly, many outdoor environments are already instrumented with hardware such as street cameras. In this work, we explore the idea of repurposing existing street cameras for outdoor navigation. Our community-driven approach considers both technical and sociotechnical concerns through engagements with various stakeholders: BLV users, residents, business owners, and Community Board leadership. The resulting system, StreetNav, processes a camera's video feed using computer vision and gives BLV pedestrians real-time navigation assistance. Our evaluations show that StreetNav guides users more precisely than GPS, but its technical performance is sensitive to environmental occlusions and distance from the camera. We discuss future implications for deploying such systems at scale.



### WorldScribe: Towards Context-Aware Live Visual Descriptions
BEST_PAPER

Authors: Ruei-Che Chang, Yuxuan Liu, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170940)

Abstract: Automated live visual descriptions can aid blind people in understanding their surroundings with autonomy and independence. However, providing descriptions that are rich, contextual, and just-in-time has been a long-standing challenge in accessibility. In this work, we develop WorldScribe, a system that generates automated live real-world visual descriptions that are customizable and adaptive to users' contexts: (i) WorldScribe's descriptions are tailored to users' intents and prioritized based on semantic relevance. (ii) WorldScribe is adaptive to visual contexts, e.g., providing consecutively succinct descriptions for dynamic scenes, while presenting longer and detailed ones for stable settings. (iii) WorldScribe is adaptive to sound contexts, e.g., increasing volume in noisy environments, or pausing when conversations start. Powered by a suite of vision, language, and sound recognition models, WorldScribe introduces a description generation pipeline that balances the tradeoffs between their richness and latency to support real-time use. The design of WorldScribe is informed by prior work on providing visual descriptions and a formative study with blind participants. Our user study and subsequent pipeline evaluation show that WorldScribe can provide real-time and fairly accurate visual descriptions to facilitate environment understanding that is adaptive and customized to users' contexts. Finally, we discuss the implications and further steps toward making live visual descriptions more context-aware and humanized.



### CookAR: Affordance Augmentations in Wearable AR to Support Kitchen Tool Interactions for People with Low Vision
Authors: Jaewook Lee, Andrew Tjahjadi, Jiho Kim, Junpu Yu, Minji Park, Jiawen Zhang, Jon Froehlich, Yapeng Tian, Yuhang Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/170874)

Abstract: Cooking is a central activity of daily living, supporting independence as well as mental and physical health. However, prior work has highlighted key barriers for people with low vision (LV) to cook, particularly around safely interacting with tools, such as sharp knives or hot pans. Drawing on recent advancements in computer vision (CV), we present CookAR, a head-mounted AR system with real-time object affordance augmentations to support safe and efficient interactions with kitchen tools. To design and implement CookAR, we collected and annotated the first egocentric dataset of kitchen tool affordances, fine-tuned an affordance segmentation model, and developed an AR system with a stereo camera to generate visual augmentations. To validate CookAR, we conducted a technical evaluation of our fine-tuned model as well as a qualitative lab study with 10 LV participants for suitable augmentation design. Our technical evaluation demonstrates that our model outperforms the baseline on our tool affordance dataset, while our user study indicates a preference for affordance augmentations over the traditional whole object augmentations.



### DesignChecker: Visual Design Support for Blind and Low Vision Web Developers
Authors: Mina Huh, Amy Pavel

[Link](https://programs.sigchi.org/uist/2024/program/content/170953)

Abstract: Blind and low vision (BLV) developers create websites to share knowledge and showcase their work. A well-designed website can engage audiences and deliver information effectively, yet it remains challenging for BLV developers to review their web designs. We conducted interviews with BLV developers (N=9) and analyzed 20 websites created by BLV developers. BLV developers created highly accessible websites but wanted to assess the usability of their websites for sighted users and follow the design standards of other websites. They also encountered challenges using screen readers to identify illegible text, misaligned elements, and inharmonious colors. We present DesignChecker, a browser extension that helps BLV developers improve their web designs. With DesignChecker, users can assess their current design by comparing it to visual design guidelines, a reference website of their choice, or a set of similar websites. DesignChecker also identifies the specific HTML elements that violate design guidelines and suggests CSS changes for improvements. Our user study participants (N=8) recognized more visual design errors than using their typical workflow and expressed enthusiasm about using DesignChecker in the future.




## Dynamic Objects & Materials
### MagneDot: Integrated Fabrication and Actuation Methods of Dot-Based Magnetic Shape Displays
Authors: Lingyun Sun, Yitao Fan, Boyu Feng, Yifu Zhang, Deying Pan, Yiwen Ren, Yuyang Zhang, Qi Wang, Ye Tao, Guanyun Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170860)

Abstract: This paper presents MagneDot, a novel method for making interactive magnetic shape displays through an integrated fabrication process. Magnetic soft materials can potentially create fast, responsive morphing structures for interactions. However, novice users and designers typically do not have access to sophisticated equipment and materials or cannot afford heavy labor to create interactive objects based on this material. Modified from an open-source 3D printer, the fabrication system of MagneDot integrates the processes of mold-making, pneumatic extrusion, magnetization, and actuation, using cost-effective materials only. By providing a design tool, MagneDot allows users to generate G-codes for fabricating and actuating displays of various morphing effects. Finally, a series of design examples demonstrate the possibilities of shape displays enabled by MagneDot.



### CARDinality: Interactive Card-shaped Robots with Locomotion and Haptics using Vibration
Authors: Aditya Retnanto, Emilie Faracci, Anup Sathya, Yu-Kai Hung, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170995)

Abstract: This paper introduces a novel approach to interactive robots by leveraging the form-factor of cards to create thin robots equipped with vibrational capabilities for locomotion and haptic feedback. The system is composed of flat-shaped robots with on-device sensing and wireless control, which offer lightweight portability and scalability. This research introduces a hardware prototype to explore the possibility of ‘vibration-based omni-directional sliding locomotion’. Applications include augmented card playing, educational tools, and assistive technology, which showcase CARDinality’s versatility in tangible interaction.




### PortaChrome: A Portable Contact Light Source for Integrated Re-Programmable Multi-Color Textures
Authors: Yunyi Zhu, Cedric Honnet, Yixiao Kang, Junyi Zhu, Angelina Zheng, Kyle Heinz, Grace Tang, Luca Musk, Michael Wessely, Stefanie Mueller

[Link](https://programs.sigchi.org/uist/2024/program/content/170742)

Abstract: In this paper, we present PortaChrome, a portable light source that can be attached to everyday objects to reprogram the color and texture of surfaces that come in contact with them. When PortaChrome makes contact with objects previously coated with photochromic dye, the UV and RGB LEDs inside PortaChrome create multi-color textures on the objects. In contrast to prior work, which used projectors for the color-change, PortaChrome has a thin and flexible form factor, which allows the color-change process to be integrated into everyday user interaction. Because of the close distance between the light source and the photochromic object, PortaChrome creates color textures in less than 4 minutes on average, which is 8 times faster than prior work. We demonstrate PortaChrome with four application examples, including data visualizations on textiles and dynamic designs on wearables. 



### Augmented Object Intelligence with XR-Objects
Authors: Mustafa Doga Dogan, Eric Gonzalez, Karan Ahuja, Ruofei Du, Andrea Colaço, Johnny Lee, Mar Gonzalez-Franco, David Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170733)

Abstract: Seamless integration of physical objects as interactive digital entities remains a challenge for spatial computing. This paper explores Augmented Object Intelligence (AOI) in the context of XR, an interaction paradigm that aims to blur the lines between digital and physical by equipping real-world objects with the ability to interact as if they were digital, where every object has the potential to serve as a portal to digital functionalities. Our approach utilizes real-time object segmentation and classification, combined with the power of Multimodal Large Language Models (MLLMs), to facilitate these interactions without the need for object pre-registration. We implement the AOI concept in the form of XR-Objects, an open-source prototype system that provides a platform for users to engage with their physical environment in contextually relevant ways using object-based context menus. This system enables analog objects to not only convey information but also to initiate digital actions, such as querying for details or executing tasks. Our contributions are threefold: (1) we define the AOI concept and detail its advantages over traditional AI assistants, (2) detail the XR-Objects system’s open-source design and implementation, and (3) show its versatility through various use cases and a user study.




## Generating Visuals
### ShadowMagic: Designing Human-AI Collaborative Support for Comic Professionals’ Shadowing
Authors: Amrita Ganguly, Chuan Yan, John Chung, Tong Sun, YOON KIHEON, Yotam Gingold, Sungsoo Ray Hong

[Link](https://programs.sigchi.org/uist/2024/program/content/170726)

Abstract: Shadowing allows artists to convey realistic volume and emotion of characters in comic colorization. While AI technologies have the potential to improve professionals’ shadowing experience, current practice is manual and time-consuming. To understand how we can improve their shadowing experience, we conducted interviews with 5 professionals. We found that professionals’ level of engagement can vary depending on semantics, such as characters’ faces or hair. We also found they spent time on shadow “landscaping”—deciding where to place large shadow regions to create a realistic volumetric presentation while the final results can vary dramatically depending on their “staging” and “attention guiding” needs. We discovered they would accept AI suggestions for less engaging semantic parts or landscaping, while needing the capability to adjust details. Based on our observations, we developed ShadowMagic, which (1) generates AI-driven shadows based on commonly used light directions, (2) enables users to selectively choose results depending on semantics, and (3) allows users to complete shadow areas themselves for further perfection. Through a summative evaluation with 5 professionals, we found that they were significantly more satisfied with our AI-driven results compared to a baseline. We also found that ShadowMagic’s “step by step” workflow helps participants more easily adopt AI-driven results. We conclude by providing implications.



### What's the Game, then? Opportunities and Challenges for Runtime Behavior Generation
BEST_PAPER

Authors: Nicholas Jennings, Han Wang, Isabel Li, James Smith, Bjoern Hartmann

[Link](https://programs.sigchi.org/uist/2024/program/content/170924)

Abstract: Procedural content generation (PCG), the process of algorithmically creating game components instead of manually, has been a common tool of game development for decades. Recent advances in large language models (LLMs) enable the generation of game behaviors based on player input at runtime. Such code generation brings with it the possibility of entirely new gameplay interactions that may be difficult to integrate with typical game development workflows. We explore these implications through GROMIT, a novel LLM-based runtime behavior generation system for Unity. When triggered by a player action, GROMIT generates a relevant behavior which is compiled without developer intervention and incorporated into the game. We create three demonstration scenarios with GROMIT to investigate how such a technology might be used in game development. In a system evaluation we find that our implementation is able to produce behaviors that result in significant downstream impacts to gameplay. We then conduct an interview study with n=13 game developers using GROMIT as a probe to elicit their current opinion on runtime behavior generation tools, and enumerate the specific themes curtailing the wider use of such tools. We find that the main themes of concern are quality considerations, community expectations, and fit with developer workflows, and that several of the subthemes are unique to runtime behavior generation specifically. We outline a future work agenda to address these concerns, including the need for additional guardrail systems for behavior generation.



### StyleFactory: Towards Better Style Alignment in Image Creation through Style-Strength-Based Control and Evaluation
Authors: Mingxu Zhou, Dengming Zhang, Weitao You, Ziqi Yu, Yifei Wu, Chenghao Pan, Huiting Liu, Tianyu Lao, Pei Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170929)

Abstract: Generative AI models have been widely used for image creation. However, generating images that are well-aligned with users' personal styles on aesthetic features (e.g., color and texture) can be challenging due to the poor style expression and interpretation between humans and models. Through a formative study, we observed that participants showed a clear subjective perception of the desired style and variations in its strength, which directly inspired us to develop style-strength-based control and evaluation. Building on this, we present StyleFactory, an interactive system that helps users achieve style alignment. Our interface enables users to rank images based on their strengths in the desired style and visualizes the strength distribution of other images in that style from the model's perspective. In this way, users can evaluate the understanding gap between themselves and the model, and define well-aligned personal styles for image creation through targeted iterations. Our technical evaluation and user study demonstrate that StyleFactory accurately generates images in specific styles, effectively facilitates style alignment in image creation workflow, stimulates creativity, and enhances the user experience in human-AI interactions.



### AutoSpark: Supporting Automobile Appearance Design Ideation with Kansei Engineering and Generative AI
Authors: Liuqing Chen, Qianzhi Jing, Yixin Tsang, Qianyi Wang, Ruocong Liu, Duowei Xia, Yunzhan Zhou, Lingyun Sun

[Link](https://programs.sigchi.org/uist/2024/program/content/170878)

Abstract: Rapid creation of novel product appearance designs that align with consumer emotional requirements poses a significant challenge. Text-to-image models, with their excellent image generation capabilities, have demonstrated potential in providing inspiration to designers. However, designers still encounter issues including aligning emotional needs, expressing design intentions, and comprehending generated outcomes in practical applications. To address these challenges, we introduce AutoSpark, an interactive system that integrates Kansei Engineering and generative AI to provide creativity support for designers in creating automobile appearance designs that meet emotional needs. AutoSpark employs a Kansei Engineering engine powered by generative AI and a semantic network to assist designers in emotional need alignment, design intention expression, and prompt crafting. It also facilitates designers' understanding and iteration of generated results through fine-grained image-image similarity comparisons and text-image relevance assessments. The design-thinking map within its interface aids in managing the design process. Our user study indicates that AutoSpark effectively aids designers in producing designs that are more aligned with emotional needs and of higher quality compared to a baseline system, while also enhancing the designers' experience in the human-AI co-creation process.




## Movement-based UIs
### Feminist Interaction Techniques: Social Consent Signals to Deter NCIM Screenshots
Authors: Li Qiwei, Francesca Lameiro, Shefali Patel, Cristi Isaula-Reyes, Eytan Adar, Eric Gilbert, Sarita Schoenebeck

[Link](https://programs.sigchi.org/uist/2024/program/content/170858)

Abstract: Non-consensual Intimate Media (NCIM) refers to the distribution of sexual or intimate content without consent. NCIM is common and causes significant emotional, financial, and reputational harm. We developed Hands-Off, an interaction technique for messaging applications that deters non-consensual screenshots. Hands-Off requires recipients to perform a hand gesture in the air, above the device, to unlock media—which makes simultaneous screenshotting difficult. A lab study shows that Hands-Off gestures are easy
to perform and reduce non-consensual screenshots by 67%. We conclude by generalizing this approach and introduce the idea of Feminist Interaction Techniques (FIT), interaction techniques that encode feminist values and speak to societal problems, and reflect on FIT’s opportunities and limitations.



### Effects of Computer Mouse Lift-off Distance Settings in Mouse Lifting Action
Authors: Munjeong Kim, Sunjun Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170957)

Abstract: This study investigates the effect of Lift-off Distance (LoD) on a computer mouse, which refers to the height at which a mouse sensor stops tracking when lifted off the surface. Although a low LoD is generally preferred to avoid unintentional cursor movement in mouse lifting (=clutching), especially in first-person shooter games, it may reduce tracking stability. 
We conducted a psychophysical experiment to measure the perceptible differences between LoD levels and quantitatively measured the unintentional cursor movement error and tracking stability at four levels of LoD while users performed mouse lifting. The results showed a trade-off between movement error and tracking stability at varying levels of LoD. Our findings offer valuable information on optimal LoD settings, which could serve as a guide for choosing a proper mouse device for enthusiastic gamers. 



### DisMouse: Disentangling Information from Mouse Movement Data
Authors: Guanhua Zhang, Zhiming Hu, Andreas Bulling

[Link](https://programs.sigchi.org/uist/2024/program/content/170847)

Abstract: Mouse movement data contain rich information about users, performed tasks, and user interfaces, but separating the respective components remains challenging and unexplored. As a first step to address this challenge, we propose DisMouse – the first method to disentangle user-specific and user-independent information and stochastic variations from mouse movement data. At the core of our method is an autoencoder trained in a semi-supervised fashion, consisting of a self-supervised denoising diffusion process and a supervised contrastive user identification module. Through evaluations on three datasets, we show that DisMouse 1) captures complementary information of mouse input, hence providing an interpretable framework for modelling mouse movements, 2) can be used to produce refined features, thus enabling various applications such as personalised and variable mouse data generation, and 3) generalises across different datasets. Taken together, our results underline the significant potential of disentangled representation learning for explainable, controllable, and generalised mouse behaviour modelling.



### Wheeler: A Three-Wheeled Input Device for Usable, Efficient, and Versatile Non-Visual Interaction
HONORABLE_MENTION

Authors: Md Touhidul Islam, Noushad Sojib, Imran Kabir, Ashiqur Rahman Amit, Mohammad Ruhul Amin, Syed Masum Billah

[Link](https://programs.sigchi.org/uist/2024/program/content/170848)

Abstract: Blind users rely on keyboards and assistive technologies like screen readers to interact with user interface (UI) elements. In modern applications with complex UI hierarchies, navigating to different UI elements poses a significant accessibility challenge. Users must listen to screen reader audio descriptions and press relevant keyboard keys one at a time. This paper introduces Wheeler, a novel three-wheeled, mouse-shaped stationary input device, to address this issue. Informed by participatory sessions, Wheeler enables blind users to navigate up to three hierarchical levels in an app independently using three wheels instead of navigating just one level at a time using a keyboard. The three wheels also offer versatility, allowing users to repurpose them for other tasks, such as 2D cursor manipulation. A study with 12 blind users indicates a significant reduction (40%) in navigation time compared to using a keyboard. Further, a diary study with our blind co-author highlights Wheeler's additional benefits, such as accessing UI elements with partial metadata and facilitating mixed-ability collaboration.




## Hacking Perception
### Predicting the Limits: Tailoring Unnoticeable Hand Redirection Offsets in Virtual Reality to Individuals’ Perceptual Boundaries
Authors: Martin Feick, Kora Regitz, Lukas Gehrke, André Zenner, Anthony Tang, Tobias Jungbluth, Maurice Rekrut, Antonio Krüger

[Link](https://programs.sigchi.org/uist/2024/program/content/171017)

Abstract: Many illusion and interaction techniques in Virtual Reality (VR) rely on Hand Redirection (HR), which has proved to be effective as long as the introduced offsets between the position of the real and virtual hand do not noticeably disturb the user experience. Yet calibrating HR offsets is a tedious and time-consuming process involving psychophysical experimentation, and the resulting thresholds are known to be affected by many variables---limiting HR's practical utility. As a result, there is a clear need for alternative methods that allow tailoring HR to the perceptual boundaries of individual users. We conducted an experiment with 18 participants combining movement, eye gaze and EEG data to detect HR offsets Below, At, and Above individuals' detection thresholds. Our results suggest that we can distinguish HR At and Above from no HR. Our exploration provides a promising new direction with potentially strong implications for the broad field of VR illusions.



### Modulating Heart Activity and Task Performance using Haptic Heartbeat Feedback: A Study Across Four Body Placements
Authors: Andreia Valente, Dajin Lee, Seungmoon Choi, Mark Billinghurst, Augusto Esteves

[Link](https://programs.sigchi.org/uist/2024/program/content/170839)

Abstract: This paper explores the impact of vibrotactile haptic feedback on heart activity when the feedback is provided at four different body locations (chest, wrist, neck, and ankle) and with two feedback rates (50 bpm and 110 bpm). A user study found that the neck placement resulted in higher heart rates and lower heart rate variability, and higher frequencies correlated with increased heart rates and decreased heart rate variability. The chest was preferred in self-reported metrics, and neck placement was perceived as less satisfying, harmonious, and immersive. This research contributes to understanding the interplay between psychological experiences and physiological responses when using haptic biofeedback resembling real body signals. 



### Augmented Breathing via Thermal Feedback in the Nose
Authors: Jas Brooks, Alex Mazursky, Janice Hixon, Pedro Lopes

[Link](https://programs.sigchi.org/uist/2024/program/content/170728)

Abstract: We propose, engineer, and study a novel method to augment the feeling of breathing—enabling interactive applications to let users feel like they are inhaling more/less air (perceived nasal airflow). We achieve this effect by cooling or heating the nose in sync with the user’s inhalation. Our illusion builds on the physiology of breathing: we perceive our breath predominantly through the cooling of our nasal cavities during inhalation. This is why breathing in a “fresh” cold environment feels easier than in a “stuffy” hot environment, even when the inhaled volume is the same. Our psychophysical study confirmed that our in-nose temperature stimulation significantly influenced breathing perception in both directions: making it feel harder & easier to breathe. Further, we found that ~90% of the trials were described as a change in perceived airflow/breathing, while only ~8% as temperature. Following, we engineered a compact device worn across the septum that uses Peltier elements. We illustrate the potential of this augmented breathing in interactive contexts, such as for virtual reality (e.g., rendering ease of breathing crisp air or difficulty breathing with a deteriorated gas mask) and everyday interactions (e.g., in combination with a relaxation application or to alleviate the perceived breathing resistance when wearing a mask).



### Thermal In Motion: Designing Thermal Flow Illusions with Tactile and Thermal Interaction
Authors: Yatharth Singhal, Daniel Honrales, Haokun Wang, Jin Ryong Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170896)

Abstract: This study presents a novel method for creating moving thermal sensations by integrating the thermal referral illusion with tactile motion. Conducted through three experiments on human forearms, the first experiment examined the impact of temperature and thermal actuator placement on perceived thermal motion, finding the clearest perception with a centrally positioned actuator under both hot and cold conditions. The second experiment identified the speed thresholds of perceived thermal motion, revealing a wider detectable range in hot conditions (1.8 cm/s to 9.5cm/s) compared to cold conditions (2.4cm/s to 5.0cm/s). Finally, we integrated our approach into virtual reality (VR) to assess its feasibility through two interaction scenarios. Our results shed light on the comprehension of thermal perception and its integration with tactile cues, promising significant advancements in incorporating thermal motion into diverse thermal interfaces for immersive VR experiences.




## New realities
### SIM2VR: Towards Automated Biomechanical Testing in VR
Authors: Florian Fischer, Aleksi Ikkala, Markus Klar, Arthur Fleig, Miroslav Bachinski, Roderick Murray-Smith, Perttu Hämäläinen, Antti Oulasvirta, Jörg Müller

[Link](https://programs.sigchi.org/uist/2024/program/content/170989)

Abstract: Automated biomechanical testing has great potential for the development of VR applications, as initial insights into user behaviour can be gained in silico early in the design process.
In particular, it allows prediction of user movements and ergonomic variables, such as fatigue, prior to conducting user studies.
However, there is a fundamental disconnect between simulators hosting state-of-the-art biomechanical user models and simulators used to develop and run VR applications. 
Existing user simulators often struggle to capture the intricacies of real-world VR applications, reducing ecological validity of user predictions.
In this paper, we introduce SIM2VR, a system that aligns user simulation with a given VR application by establishing a continuous closed loop between the two processes.
This, for the first time, enables training simulated users directly in the same VR application that real users interact with.
We demonstrate that SIM2VR can predict differences in user performance, ergonomics and strategies in a fast-paced, dynamic arcade game. In order to expand the scope of automated biomechanical testing beyond simple visuomotor tasks, advances in cognitive models and reward function design will be needed.



### Hands-on, Hands-off: Gaze-Assisted Bimanual 3D Interaction
Authors: Mathias Lystbæk, Thorbjørn Mikkelsen, Roland Krisztandl, Eric Gonzalez, Mar Gonzalez-Franco, Hans Gellersen, Ken Pfeuffer

[Link](https://programs.sigchi.org/uist/2024/program/content/171002)

Abstract: Extended Reality (XR) systems with hand-tracking support direct manipulation of objects with both hands. A common interaction in this context is for the non-dominant hand (NDH) to orient an object for input by the dominant hand (DH). We explore bimanual interaction with gaze through three new modes of interaction where the input of the NDH, DH, or both hands is indirect based on Gaze+Pinch. These modes enable a new dynamic interplay between our hands, allowing flexible alternation between and pairing of complementary operations. Through applications, we demonstrate several use cases in the context of 3D modelling, where users exploit occlusion-free, low-effort, and fluid two-handed manipulation. To gain a deeper understanding of each mode, we present a user study on an asymmetric rotate-translate task. Most participants preferred indirect input with both hands for lower physical effort, without a penalty on user performance. Otherwise, they preferred modes where the NDH oriented the object directly, supporting preshaping of the hand, which is more challenging with indirect gestures. The insights gained are of relevance for the design of XR interfaces that aim to leverage eye and hand input in tandem.



### Pro-Tact: Hierarchical Synthesis of Proprioception and Tactile Exploration for Eyes-Free Ray Pointing on Out-of-View VR Menus
Authors: Yeonsu Kim, Jisu Yim, Kyunghwan Kim, Yohan Yun, Geehyuk Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170805)

Abstract: We introduce Pro-Tact, a novel eyes-free pointing technique for interacting with out-of-view (OoV) VR menus. This technique combines rapid rough pointing using proprioception with fine-grain adjustments through tactile exploration, enabling menu interaction without visual attention. Our user study demonstrated that Pro-Tact allows users to select menu items accurately (95% accuracy for 54 items) in an eyes-free manner, with reduced fatigue and sickness compared to eyes-engaged interaction. Additionally, we observed that participants voluntarily interacted with OoV menus eyes-free when Pro-Tact's tactile feedback was provided in practical VR application usage contexts. This research contributes by introducing the novel interaction technique, Pro-Tact, and quantitatively evaluating its benefits in terms of performance, user experience, and user preference in OoV menu interactions.



### GradualReality: Enhancing Physical Object Interaction in Virtual Reality via Interaction State-Aware Blending
Authors: HyunA Seo, Juheon Yi, Rajesh Balan, Youngki Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170920)

Abstract: We present GradualReality, a novel interface enabling a Cross Reality experience that includes gradual interaction with physical objects in a virtual environment and supports both presence and usability. Daily Cross Reality interaction is challenging as the user's physical object interaction state is continuously changing over time, causing their attention to frequently shift between the virtual and physical worlds. As such, presence in the virtual environment and seamless usability for interacting with physical objects should be maintained at a high level. To address this issue, we present an Interaction State-Aware Blending approach that (i) balances immersion and interaction capability and (ii) provides a fine-grained, gradual transition between virtual and physical worlds. The key idea includes categorizing the flow of physical object interaction into multiple states and designing novel blending methods that offer optimal presence and sufficient physical awareness at each state. We performed extensive user studies and interviews with a working prototype and demonstrated that GradualReality provides better Cross Reality experiences compared to baselines.



### StegoType: Surface Typing from Egocentric Cameras
Authors: Mark Richardson, Fadi Botros, Yangyang Shi, Pinhao Guo, Bradford Snow, Linguang Zhang, Jingming Dong, Keith Vertanen, Shugao Ma, Robert Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170853)

Abstract: Text input is a critical component of any general purpose computing system, yet efficient and natural text input remains a challenge in AR and VR. Headset based hand-tracking has recently become pervasive among consumer VR devices and affords the opportunity to enable touch typing on virtual keyboards. We present an approach for decoding touch typing on uninstrumented flat surfaces using only egocentric camera-based hand-tracking as input. While egocentric hand-tracking accuracy is limited by issues like self occlusion and image fidelity, we show that a sufficiently diverse training set of hand motions paired with typed text can enable a deep learning model to extract signal from this noisy input. 
Furthermore, by carefully designing a closed-loop data collection process, we can train an end-to-end text decoder that accounts for natural sloppy typing on virtual keyboards.  
We evaluate our work with a user study (n=18) showing a mean online throughput of 42.4 WPM with an uncorrected error rate (UER) of 7% with our method compared to a physical keyboard baseline of 74.5 WPM at 0.8% UER, showing progress towards unlocking productivity and high throughput use cases in AR/VR.



### Eye-Hand Movement of Objects in Near Space Extended Reality
Authors: Uta Wagner, Andreas Asferg Jacobsen, Tiare Feuchtner, Hans Gellersen, Ken Pfeuffer

[Link](https://programs.sigchi.org/uist/2024/program/content/170771)

Abstract: Hand-tracking in Extended Reality (XR) enables moving objects in near space with direct hand gestures, to pick, drag and drop objects in 3D. In this work, we investigate the use of eye-tracking to reduce the effort involved in this interaction. As the eyes naturally look ahead to the target for a drag operation, the principal idea is to map the translation of the object in the image plane to gaze, such that the hand only needs to control the depth component of the operation. We have implemented four techniques that explore two factors: the use of gaze only to move objects in X-Y vs.\ extra refinement by hand, and the use of hand input in 
 the Z axis to directly move objects vs.\ indirectly via a transfer function. We compared all four techniques in a user study (N=24) against baselines of direct and indirect hand input. We detail user performance, effort and experience trade-offs and show that all eye-hand techniques significantly reduce physical effort over direct gestures, pointing toward effortless drag-and-drop for XR environments.




## Prototyping
### ProtoDreamer: A Mixed-prototype Tool Combining Physical Model and Generative AI to Support Conceptual Design
Authors: Hongbo ZHANG, Pei Chen, Xuelong Xie, Chaoyi Lin, Lianyan Liu, Zhuoshu Li, Weitao You, Lingyun Sun

[Link](https://programs.sigchi.org/uist/2024/program/content/170974)

Abstract: Prototyping serves as a critical phase in the industrial conceptual design process, enabling exploration of problem space and identification of solutions. Recent advancements in large-scale generative models have enabled AI to become a co-creator in this process. However, designers often consider generative AI challenging due to the necessity to follow computer-centered interaction rules, diverging from their familiar design materials and languages. Physical prototype is a commonly used design method, offering unique benefits in prototype process, such as intuitive understanding and tangible testing. In this study, we propose ProtoDreamer, a mixed-prototype tool that synergizes generative AI with physical prototype to support conceptual design. ProtoDreamer allows designers to construct preliminary prototypes using physical materials, while AI recognizes these forms and vocal inputs to generate diverse design alternatives. This tool empowers designers to tangibly interact with prototypes, intuitively convey design intentions to AI, and continuously draw inspiration from the generated artifacts. An evaluation study confirms ProtoDreamer’s utility and strengths in time efficiency, creativity support, defects exposure, and detailed thinking facilitation.



### TorqueCapsules: Fully-Encapsulated Flywheel Actuation Modules for Designing and Prototyping Movement-Based and Kinesthetic Interaction
Authors: Willa Yunqi Yang, Yifan Zou, Jingle Huang, Raouf Abujaber, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170857)

Abstract: Flywheels are unique, versatile actuators that store and convert kinetic energy to torque, widely utilized in aerospace, robotics, haptics, and more. However, prototyping interaction using flywheels is not trivial due to safety concerns, unintuitive operation, and implementation challenges. 
We present TorqueCapsules: self-contained, fully-encapsulated flywheel actuation modules that make the flywheel actuators easy to control, safe to interact with, and quick to reconfigure and customize. By fully encapsulating the actuators with a wireless microcontroller, a battery, and other components, the module can be readily attached, embedded, or stuck to everyday objects, worn to people’s bodies, or combined with other devices. With our custom GUI, both novices and expert users can easily control multiple modules to design and prototype movements and kinesthetic haptics unique to flywheel actuation. We demonstrate various applications, including actuated everyday objects, wearable haptics, and expressive robots. We conducted workshops for novices and experts to employ TorqueCapsules to collect qualitative feedback and further application examples.



### AniCraft: Crafting Everyday Objects as Physical Proxies for Prototyping 3D Character Animation in Mixed Reality
Authors: Boyu Li, Linping Yuan, Zhe Yan, Qianxi Liu, Yulin Shen, Zeyu Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170881)

Abstract: We introduce AniCraft, a mixed reality system for prototyping 3D character animation using physical proxies crafted from everyday objects. Unlike existing methods that require specialized equipment to support the use of physical proxies, AniCraft only requires affordable markers, webcams, and daily accessible objects and materials. AniCraft allows creators to prototype character animations through three key stages: selection of virtual characters, fabrication of physical proxies, and manipulation of these proxies to animate the characters. This authoring workflow is underpinned by diverse physical proxies, manipulation types, and mapping strategies, which ease the process of posing virtual characters and mapping user interactions with physical proxies to animated movements of virtual characters. We provide a range of cases and potential applications to demonstrate how diverse physical proxies can inspire user creativity. User experiments show that our system can outperform traditional animation methods for rapid prototyping. Furthermore, we provide insights into the benefits and usage patterns of different materials, which lead to design implications for future research.



### Mul-O: Encouraging Olfactory Innovation in Various Scenarios Through a Task-Oriented Development Platform
Authors: Peizhong Gao, Fan Liu, Di Wen, Yuze Gao, Linxin Zhang, Chikelei Wang, Qiwei Zhang, Yu Zhang, Shao-en Ma, Qi Lu, Haipeng Mi, YINGQING XU

[Link](https://programs.sigchi.org/uist/2024/program/content/170886)

Abstract: Olfactory interfaces are pivotal in HCI, yet their development is hindered by limited application scenarios, stifling the discovery of new research opportunities. This challenge primarily stems from existing design tools focusing predominantly on odor display devices and the creation of standalone olfactory experiences, rather than enabling rapid adaptation to various contexts and tasks. Addressing this, we introduce Mul-O, a novel task-oriented development platform crafted to aid semi-professionals in navigating the diverse requirements of potential application scenarios and effectively prototyping ideas.
Mul-O facilitates the swift association and integration of olfactory experiences into functional designs, system integrations, and concept validations. Comprising a web UI for task-oriented development, an API server for seamless third-party integration, and wireless olfactory display hardware, Mul-O significantly enhances the ideation and prototyping process in multisensory tasks. This was verified by a 15-day workshop attended by 30 participants. The workshop produced seven innovative projects, underscoring Mul-O's efficacy in fostering olfactory innovation.




## Sustainable Interfaces
### Degrade to Function: Towards Eco-friendly Morphing Devices that Function Through Programmed Sequential Degradation
Authors: Qiuyu Lu, Semina Yi, Mengtian Gan, Jihong Huang, Xiao Zhang, Yue Yang, Chenyi Shen, Lining Yao

[Link](https://programs.sigchi.org/uist/2024/program/content/170959)

Abstract: While it seems counterintuitive to think of degradation within an operating device as beneficial, one may argue that when rationally designed, the controlled breakdown of materials—physical, chemical, or biological—can be harnessed for specific functions. To apply this principle to the design of morphing devices, we introduce the concept of "Degrade to Function" (DtF). This concept aims to create eco-friendly and self-contained morphing devices that operate through a sequence of environmentally-triggered degradations. We explore its design considerations and implementation techniques by identifying environmental conditions and degradation types that can be exploited, evaluating potential materials capable of controlled degradation, suggesting designs for structures that can leverage degradation to achieve various transformations and functions, and developing sequential control approaches that integrate degradation triggers. To demonstrate the viability and versatility of this design strategy, we showcase several application examples across a range of environmental conditions.



### WasteBanned: Supporting Zero Waste Fashion Design Through Linked Edits
Authors: Ruowang Zhang, Stefanie Mueller, Gilbert Bernstein, Adriana Schulz, Mackenzie Leake

[Link](https://programs.sigchi.org/uist/2024/program/content/170976)

Abstract: The commonly used cut-and-sew garment construction process, in which 2D fabric panels are cut from sheets of fabric and assembled into 3D garments, contributes to widespread textile waste in the fashion industry. There is often a significant divide between the design of the garment and the layout of the panels. One opportunity for bridging this gap is the emerging study and practice of zero waste fashion design, which involves creating clothing designs with maximum layout efficiency. Enforcing the strict constraints of zero waste sewing is challenging, as edits to one region of the garment necessarily affect neighboring panels. Based on our formative work to understand this emerging area within fashion design, we present WasteBanned, a tool that combines CAM and CAD to help users prioritize efficient material usage, work within these zero waste constraints, and edit existing zero waste garment patterns. Our user evaluation indicates that our tool helps fashion designers edit zero waste patterns to fit different bodies and add stylistic variation, while creating highly efficient fabric layouts.



### HoloChemie - Sustainable Fabrication of Soft Biochemical Holographic Devices for Ubiquitous Sensing
Authors: Sutirtha Roy, Moshfiq-Us-Saleheen Chowdhury, Jurjaan Noim, Richa Pandey, Aditya Shekhar Nittala

[Link](https://programs.sigchi.org/uist/2024/program/content/170931)

Abstract: Sustainable fabrication approaches and biomaterials are increasingly being used in HCI to fabricate interactive devices. However, the majority of the work has focused on integrating electronics. This paper takes a sustainable approach to exploring the fabrication of biochemical sensing devices. Firstly, we contribute a set of biochemical formulations for biological and environmental sensing with bio-sourced and environment-friendly substrate materials. Our formulations are based on a combination of enzymes derived from bacteria and fungi, plant extracts and commercially available chemicals to sense both liquid and gaseous analytes: glucose, lactic acid, pH levels and carbon dioxide. Our novel holographic sensing scheme allows for detecting the presence of analytes and enables quantitative estimation of the analyte levels. We present a set of application scenarios that demonstrate the versatility of our approach and discuss the sustainability aspects, its limitations, and the implications for bio-chemical systems in HCI.




## Sound & Music
### SonoHaptics: An Audio-Haptic Cursor for Gaze-Based Object Selection in XR
Authors: Hyunsung Cho, Naveen Sendhilnathan, Michael Nebeling, Tianyi Wang, Purnima Padmanabhan, Jonathan Browder, David Lindlbauer, Tanya Jonker, Kashyap Todi

[Link](https://programs.sigchi.org/uist/2024/program/content/170927)

Abstract: We introduce SonoHaptics, an audio-haptic cursor for gaze-based 3D object selection. SonoHaptics addresses challenges around providing accurate visual feedback during gaze-based selection in Extended Reality (XR), e.g., lack of world-locked displays in no- or limited-display smart glasses and visual inconsistencies. To enable users to distinguish objects without visual feedback, SonoHaptics employs the concept of cross-modal correspondence in human perception to map visual features of objects (color, size, position, material) to audio-haptic properties (pitch, amplitude, direction, timbre). We contribute data-driven models for determining cross-modal mappings of visual features to audio and haptic features, and a computational approach to automatically generate audio-haptic feedback for objects in the user's environment. SonoHaptics provides global feedback that is unique to each object in the scene, and local feedback to amplify differences between nearby objects. Our comparative evaluation shows that SonoHaptics enables accurate object identification and selection in a cluttered scene without visual feedback.



### SonifyAR: Context-Aware Sound Generation in Augmented Reality
Authors: Xia Su, Jon Froehlich, Eunyee Koh, Chang Xiao

[Link](https://programs.sigchi.org/uist/2024/program/content/170866)

Abstract: Sound plays a crucial role in enhancing user experience and immersiveness in Augmented Reality (AR). However, current platforms lack support for AR sound authoring due to limited interaction types, challenges in collecting and specifying context information, and difficulty in acquiring matching sound assets. We present SonifyAR, an LLM-based AR sound authoring system that generates context-aware sound effects for AR experiences. SonifyAR expands the current design space of AR sound and implements a Programming by Demonstration (PbD) pipeline to automatically collect contextual information of AR events, including virtual-content-semantics and real-world context. This context information is then processed by a large language model to acquire sound effects with Recommendation, Retrieval, Generation, and Transfer methods. To evaluate the usability and performance of our system, we conducted a user study with eight participants and created five example applications, including an AR-based science experiment, and an assistive application for low-vision AR users.



### Auptimize: Optimal Placement of Spatial Audio Cues for Extended Reality
Authors: Hyunsung Cho, Alexander Wang, Divya Kartik, Emily Xie, Yukang Yan, David Lindlbauer

[Link](https://programs.sigchi.org/uist/2024/program/content/170952)

Abstract: Spatial audio in Extended Reality (XR) provides users with better awareness of where virtual elements are placed, and efficiently guides them to events such as notifications, system alerts from different windows, or approaching avatars. Humans, however, are inaccurate in localizing sound cues, especially with multiple sources due to limitations in human auditory perception such as angular discrimination error and front-back confusion. This decreases the efficiency of XR interfaces because users misidentify from which XR element a sound is coming. To address this, we propose Auptimize, a novel computational approach for placing XR sound sources, which mitigates such localization errors by utilizing the ventriloquist effect. Auptimize disentangles the sound source locations from the visual elements and relocates the sound sources to optimal positions for unambiguous identification of sound cues, avoiding errors due to inter-source proximity and front-back confusion. Our evaluation shows that Auptimize decreases spatial audio-based source identification errors compared to playing sound cues at the paired visual-sound locations. We demonstrate the applicability of Auptimize for diverse spatial audio-based interactive XR scenarios.



### EarHover: Mid-Air Gesture Recognition for Hearables Using Sound Leakage Signals
BEST_PAPER

Authors: Shunta Suzuki, Takashi Amesaka, Hiroki Watanabe, Buntarou Shizuki, Yuta Sugiura

[Link](https://programs.sigchi.org/uist/2024/program/content/170787)

Abstract: We introduce EarHover, an innovative system that enables mid-air gesture input for hearables. Mid-air gesture input, which eliminates the need to touch the device and thus helps to keep hands and the device clean, has been known to have high demand based on previous surveys. However, existing mid-air gesture input methods for hearables have been limited to adding cameras or infrared sensors. By focusing on the sound leakage phenomenon unique to hearables, we have realized mid-air gesture recognition using a speaker and an external microphone that are highly compatible with hearables. The signal leaked to the outside of the device due to sound leakage can be measured by an external microphone, which detects the differences in reflection characteristics caused by the hand's speed and shape during mid-air gestures.
Among 27 types of gestures, we determined the seven most suitable gestures for EarHover in terms of signal discrimination and user acceptability. We then evaluated the gesture detection and classification performance of two prototype devices (in-ear type/open-ear type) for real-world application scenarios.



### Towards Music-Aware Virtual Assistants
Authors: Alexander Wang, David Lindlbauer, Chris Donahue

[Link](https://programs.sigchi.org/uist/2024/program/content/170955)

Abstract: We propose a system for modifying spoken notifications in a manner that is sensitive to the music a user is listening to. Spoken notifications provide convenient access to rich information without the need for a screen. Virtual assistants see prevalent use in hands-free settings such as driving or exercising, activities where users also regularly enjoy listening to music. In such settings, virtual assistants will temporarily mute a user's music to improve intelligibility. However, users may perceive these interruptions as intrusive, negatively impacting their music-listening experience. To address this challenge, we propose the concept of music-aware virtual assistants, where speech notifications are modified to resemble a voice singing in harmony with the user's music. We contribute a system that processes user music and notification text to produce a blended mix, replacing original song lyrics with the notification content. In a user study comparing musical assistants to standard virtual assistants, participants expressed that musical assistants fit better with music, reduced intrusiveness, and provided a more delightful listening experience overall.





## Learning to Learn
### Patterns of Hypertext-Augmented Sensemaking
Authors: Siyi Zhu, Robert Haisfield, Brendan Langen, Joel Chan

[Link](https://programs.sigchi.org/uist/2024/program/content/170882)

Abstract: The early days of HCI were marked by bold visions of hypertext as a transformative medium for augmented sensemaking, exemplified in systems like Memex, Xanadu, and NoteCards. Today, however, hypertext is often disconnected from discussions of the future of sensemaking. In this paper, we investigate how the recent resurgence in hypertext ``tools for thought'' might point to new directions for hypertext-augmented sensemaking. Drawing on detailed analyses of guided tours with 23 scholars, we describe hypertext-augmented use patterns for dealing with the core problem of revisiting and reusing existing/past ideas during scholarly sensemaking. We then discuss how these use patterns validate and extend existing knowledge of hypertext design patterns for sensemaking, and point to new design opportunities for augmented sensemaking.



### Augmented Physics: Creating Interactive and Embedded Physics Simulations from Static Textbook Diagrams
BEST_PAPER

Authors: Aditya Gunturu, Yi Wen, Nandi Zhang, Jarin Thundathil, Rubaiat Habib Kazi, Ryo Suzuki

[Link](https://programs.sigchi.org/uist/2024/program/content/170907)

Abstract: We introduce Augmented Physics, a machine learning-integrated authoring tool designed for creating embedded interactive physics simulations from static textbook diagrams. Leveraging recent advancements in computer vision, such as Segment Anything and Multi-modal LLMs, our web-based system enables users to semi-automatically extract diagrams from physics textbooks and generate interactive simulations based on the extracted content. These interactive diagrams are seamlessly integrated into scanned textbook pages, facilitating interactive and personalized learning experiences across various physics concepts, such as optics, circuits, and kinematics. Drawing from an elicitation study with seven physics instructors, we explore four key augmentation strategies: 1) augmented experiments, 2) animated diagrams, 3) bi-directional binding, and 4) parameter visualization. We evaluate our system through technical evaluation, a usability study (N=12), and expert interviews (N=12). Study findings suggest that our system can facilitate more engaging and personalized learning experiences in physics education.



### Qlarify: Recursively Expandable Abstracts for Dynamic Information Retrieval over Scientific Papers
Authors: Raymond Fok, Joseph Chee Chang, Tal August, Amy Zhang, Daniel Weld

[Link](https://programs.sigchi.org/uist/2024/program/content/170964)

Abstract: Navigating the vast scientific literature often starts with browsing a paper’s abstract. However, when a reader seeks additional information, not present in the abstract, they face a costly cognitive chasm during their dive into the full text. To bridge this gap, we introduce recursively expandable abstracts, a novel interaction paradigm that dynamically expands abstracts by progressively incorporating additional information from the papers’ full text. This lightweight interaction allows scholars to specify their information needs by quickly brushing over the abstract or selecting AI-suggested expandable entities. Relevant information is synthesized using a retrieval-augmented generation approach, presented as a fluid, threaded expansion of the abstract, and made efficiently verifiable via attribution to relevant source-passages in the paper. Through a series of user studies, we demonstrate the utility of recursively expandable abstracts and identify future opportunities to support low-effort and just-in-time exploration of long-form information contexts through LLM-powered interactions.



### LessonPlanner: Assisting Novice Teachers to Prepare Pedagogy-Driven Lesson Plans with Large Language Models
Authors: Haoxiang Fan, Guanzheng Chen, Xingbo Wang, Zhenhui Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170883)

Abstract: Preparing a lesson plan, e.g., a detailed road map with strategies and materials for instructing a 90-minute class, is beneficial yet challenging for novice teachers. Large language models (LLMs) can ease this process by generating adaptive content for lesson plans, which would otherwise require teachers to create from scratch or search existing resources. In this work, we first conduct a formative study with six novice teachers to understand their needs for support of preparing lesson plans with LLMs. Then, we develop LessonPlanner that assists users to interactively construct lesson plans with adaptive LLM-generated content based on Gagne's nine events. Our within-subjects study (N=12) shows that compared to the baseline ChatGPT interface, LessonPlanner can significantly improve the quality of outcome lesson plans and ease users' workload in the preparation process. Our expert interviews (N=6) further demonstrate LessonPlanner's usefulness in suggesting effective teaching strategies and meaningful educational resources. We discuss concerns on and design considerations for supporting teaching activities with LLMs.




## Hot Interfaces
### Fiery Hands: Designing Thermal Glove through Thermal and Tactile Integration for Virtual Object Manipulation
Authors: Haokun Wang, Yatharth Singhal, Hyunjae Gil, Jin Ryong Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170880)

Abstract: We present a novel approach to render thermal and tactile feedback to the palm and fingertips through thermal and tactile integration. Our approach minimizes the obstruction of the palm and inner side of the fingers and enables virtual object manipulation while providing localized and global thermal feedback. By leveraging thermal actuators positioned strategically on the outer palm and back of the fingers in interplay with tactile actuators, our approach exploits thermal referral and tactile masking phenomena. Through a series of user studies, we validate the perception of localized thermal sensations across the palm and fingers, showcasing the ability to generate diverse thermal patterns. Furthermore, we demonstrate the efficacy of our approach in VR applications,  replicating diverse thermal interactions with virtual objects. This work represents significant progress in thermal interactions within VR, offering enhanced sensory immersion at an optimal energy cost.



### DexteriSync: A Hand Thermal I/O Exoskeleton for Morphing Finger Dexterity Experience
Authors: Ximing Shen, Youichi Kamiyama, Kouta Minamizawa, Jun Nishida

[Link](https://programs.sigchi.org/uist/2024/program/content/170898)

Abstract: Skin temperature is an important physiological factor for human hand dexterity. Leveraging this feature, we engineered an exoskeleton, called DexteriSync, that can dynamically adjust the user's finger dexterity and induce different thermal perceptions by modulating finger skin temperature. This exoskeleton comprises flexible silicone-copper tube segments, 3D-printed finger sockets, a 3D-printed palm base, a pump system, and a water temperature control with a storage unit. By realising an embodied experience of compromised dexterity, DexteriSync can help product designers understand the lived experience of compromised hand dexterity, such as that of the elderly and/or neurodivergent users, when designing daily necessities for them. We validated DexteriSync via a technical evaluation and two user studies, demonstrating that it can change skin temperature, dexterity, and thermal perception. An exploratory session with design students and an autistic compromised dexterity individual, demonstrated the exoskeleton provided a more realistic experience compared to video education, and allowed them to gain higher confidence in their designs. The results advocated for the efficacy of experiencing embodied compromised finger dexterity, which can promote an understanding of the related physical challenges and lead to a more persuasive design for assistive tools.



### Flip-Pelt: Motor-Driven Peltier Elements for Rapid Thermal Stimulation and Congruent Pressure Feedback in Virtual Reality
Authors: Seongjun Kang, Gwangbin Kim, Seokhyun Hwang, Jeongju Park, Ahmed Elsharkawy, SeungJun Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170885)

Abstract: This study introduces "Flip-Pelt," a motor-driven peltier device designed to provide rapid thermal stimulation and congruent pressure feedback in virtual reality (VR) environments. Our system incorporates eight motor-driven peltier elements, allowing for the flipping of preheated or cooled elements to the opposite side. In evaluating the Flip-Pelt device, we assess user ability to distinguish between heat/cold sources by their patterns and stiffness, and its impact on enhancing haptic experiences in VR content that involves contact with various thermal sources. Our findings demonstrate that rapid thermal stimulation and congruent pressure feedback provided by Flip-Pelt enhance the recognition accuracy of thermal patterns and the stiffness of virtual objects. These features also improve haptic experiences in VR scenarios through their temporal congruency between tactile and thermal stimuli. Additionally, we discuss the scalability of the Flip-Pelt system to other body parts by proposing design prototypes.



### Hydroptical Thermal Feedback: Spatial Thermal Feedback Using Visible Lights and Water
Authors: Sosuke Ichihashi, Masahiko Inami, Hsin-Ni Ho, Noura Howell

[Link](https://programs.sigchi.org/uist/2024/program/content/170722)

Abstract: We control the temperature of materials in everyday interactions, recognizing temperature's important influence on our bodies, minds, and experiences. However, thermal feedback is an under-explored modality in human-computer interaction partly due to its limited temporal (slow) and spatial (small-area and non-moving) capabilities. We introduce hydroptical thermal feedback, a spatial thermal feedback method that works by applying visible lights on body parts in water. Through physical measurements and psychophysical experiments, our results show: (1) Humans perceive thermal sensations when visible lights are cast on the skin under water, and perceived warmth is greater for lights with shorter wavelengths, (2) temporal capabilities, (3) apparent motion (spatial) of warmth and coolness sensations, and (4) hydroptical thermal feedback can support the perceptual illusion that the water itself is warmer. We propose applications, including virtual reality (VR), shared water experiences, and therapies. Overall, this paper contributes hydroptical thermal feedback as a novel method, empirical results demonstrating its unique capabilities, proposed applications, and design recommendations for using hydroptical thermal feedback. Our method introduces controlled, spatial thermal perceptions to water experiences.




## FABulous
### Facilitating the Parametric Definition of Geometric Properties in Programming-Based CAD
Authors: J Gonzalez Avila, Thomas Pietrzak, Audrey Girouard, Géry Casiez

[Link](https://programs.sigchi.org/uist/2024/program/content/170736)

Abstract: Parametric Computer-aided design (CAD) enables the creation of reusable models by integrating variables into geometric properties, facilitating customization without a complete redesign. However, creating parametric designs in programming-based CAD presents significant challenges. Users define models in a code editor using a programming language, with the application generating a visual representation in a viewport. This process involves complex programming and arithmetic expressions to describe geometric properties, linking various object properties to create parametric designs. Unfortunately, these applications lack assistance, making the process unnecessarily demanding. We propose a solution that allows users to retrieve parametric expressions from the visual representation for reuse in the code, streamlining the design process. We demonstrated this concept through a proof-of-concept implemented in the programming-based CAD application, OpenSCAD, and conducted an experiment with 11 users. Our findings suggest that this solution could significantly reduce design errors, improve interactivity and engagement in the design process, and lower the entry barrier for newcomers by reducing the mathematical skills typically required in programming-based CAD applications



### Rhapso: Automatically Embedding Fiber Materials into 3D Prints for Enhanced Interactivity
Authors: Daniel Ashbrook, Wei-Ju Lin, Nicholas Bentley, Diana Soponar, Zeyu Yan, Valkyrie Savage, Lung-Pan Cheng, Huaishu Peng, Hyunyoung Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170936)

Abstract:    We introduce Rhapso, a 3D printing system designed to embed a diverse range of continuous fiber materials within 3D objects during the printing process. This approach enables integrating properties like tensile strength, force storage and transmission, or aesthetic and tactile characteristics, directly into low-cost thermoplastic 3D prints. These functional objects can have intricate actuation, self-assembly, and sensing capabilities with little to no manual intervention. To achieve this, we modify a low-cost Fused Filament Fabrication (FFF) 3D printer, adding a stepper motor-controlled fiber spool mechanism on a gear ring above the print bed. In addition to hardware, we provide parsing software for precise fiber placement, which generates Gcode for printer operation. To illustrate the versatility of our system, we present applications that showcase its extensive design potential. Additionally, we offer comprehensive documentation and open designs, empowering others to replicate our system and explore its possibilities.




### Speed-Modulated Ironing: High-Resolution Shade and Texture Gradients in Single-Material 3D Printing
Authors: Mehmet Ozdemir, Marwa AlAlawi, Mustafa Doga Dogan, Jose Martinez Castro, Stefanie Mueller, Zjenja Doubrovski

[Link](https://programs.sigchi.org/uist/2024/program/content/170731)

Abstract: We present Speed-Modulated Ironing, a new fabrication method for programming visual and tactile properties in single-material 3D printing. We use one nozzle to 3D print and a second nozzle to reheat printed areas at varying speeds, controlling the material's temperature-response. The rapid adjustments of speed allow for fine-grained reheating, enabling high-resolution color and texture variations. We implemented our method in a tool that allows users to assign desired properties to 3D models and creates corresponding 3D printing instructions. We demonstrate our method with three temperature-responsive materials: a foaming filament, a filament with wood fibers, and a filament with cork particles.  These filaments respond to temperature by changing color, roughness, transparency, and gloss. Our technical evaluation reveals the capabilities of our method in achieving sufficient resolution and color shade range that allows surface details such as small text, photos, and QR codes on 3D-printed objects. Finally, we provide application examples demonstrating the new design capabilities enabled by Speed-Modulated Ironing.



### TRAvel Slicer: Continuous Extrusion Toolpaths for 3D Printing
Authors: Jaime Gould, Camila Friedman-Gerlicz, Leah Buechley

[Link](https://programs.sigchi.org/uist/2024/program/content/170996)

Abstract: In this paper we present Travel Reduction Algorithm (TRAvel) Slicer, which minimizes travel movements in 3D printing. Conventional slicing software generates toolpaths with many travel movements--movements without material extrusion. Some 3D printers are incapable of starting and stopping extrusion and it is difficult to impossible to control the extrusion of many materials. This makes toolpaths with travel movements unsuitable for a wide range of printers and materials. 

We developed the open-source TRAvel Slicer to enable the printing of complex 3D models on a wider range of printers and in a wider range of materials than is currently possible. TRAvel Slicer minimizes two different kinds of travel movements--what we term Inner- and Outer-Model travel. We minimize Inner-Model travel (travel within the 3D model) by generating space-filling Fermat spirals for each contiguous planar region of the model. We minimize Outer-Model travel (travels outside of the 3D model) by ordering the printing of different branches of the model, thus limiting transitions between branches. We present our algorithm and software and then demonstrate how: 1) TRAvel Slicer makes it possible to generate high-quality prints from a metal-clay material, CeraMetal, that is functionally unprintable using an off-the-shelf slicer. 2) TRAvel Slicer dramatically increases the printing efficiency of traditional plastic 3D printing compared to an off-the-shelf slicer.



### Understanding and Supporting Debugging Workflows in CAD
Authors: Felix Hähnlein, Gilbert Bernstein, Adriana Schulz

[Link](https://programs.sigchi.org/uist/2024/program/content/170944)

Abstract: One of the core promises of parametric Computer-Aided Design (CAD) is that users can easily edit their model at any point in time.
However, due to the ambiguity of changing references to intermediate, updated geometry, parametric edits can lead to reference errors which are difficult to fix in practice.
We claim that debugging reference errors remains challenging because CAD systems do not provide users with tools to understand where the error happened and how to fix it.
To address these challenges, we prototype a graphical debugging tool, DeCAD, which helps comparing CAD model states both across operations and across edits.
In a qualitative lab study, we use DeCAD as a probe to understand specific challenges that users face and what workflows they employ to overcome them.
We conclude with design implications for future debugging tool developers. 





## Haptics
### LoopBot: Representing Continuous Haptics of Grounded Objects in Room-scale VR
Authors: Tetsushi Ikeda, Kazuyuki Fujita, Kumpei Ogawa, Kazuki Takashima, Yoshifumi Kitamura

[Link](https://programs.sigchi.org/uist/2024/program/content/171016)

Abstract: In room-scale virtual reality, providing continuous haptic feedback from touching grounded objects, such as walls and handrails, has been challenging due to the user's walking range and the required force. In this study, we propose LoopBot, a novel technique to provide continuous haptic feedback from grounded objects using only a single user-following robot. Specifically, LoopBot is equipped with a loop-shaped haptic prop attached to an omnidirectional robot that scrolls to cancel out the robot's displacement, giving the user the haptic sensation that the prop is actually fixed in place, or ``grounded.'' We first introduce the interaction design space of LoopBot and, as one of its promising interaction scenarios, implement a prototype for the experience of walking while grasping handrails. A performance evaluation shows that scrolling the prop cancels $77.5\%$ of the robot's running speed on average. A preliminary user test ($N=10$) also shows that the subjective realism of the experience and the sense of the virtual handrails being grounded were significantly higher than when the prop was not scrolled. Based on these findings, we discuss possible further development of LoopBot.



### JetUnit: Rendering Diverse Force Feedback in Virtual Reality Using Water Jets
Authors: Zining Zhang, Jiasheng Li, Zeyu Yan, Jun Nishida, Huaishu Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170767)

Abstract: We propose JetUnit, a water-based VR haptic system designed to produce force feedback with a wide spectrum of intensities and frequencies through water jets. The key challenge in designing this system lies in optimizing parameters to enable the haptic device to generate force feedback that closely replicates the most intense force produced by direct water jets while ensuring the user remains dry. In this paper, we present the key design parameters of the JetUnit wearable device determined through a set of quantitative experiments and a perception study. We further conducted a user study to assess the impact of integrating our haptic solutions into virtual reality experiences. The results revealed that, by adhering to the design principles of JetUnit, the water-based haptic system is capable of delivering diverse force feedback sensations, significantly enhancing the immersive experience in virtual reality.



### Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions
Authors: Takeru Hashimoto, Yutaro Hirao

[Link](https://programs.sigchi.org/uist/2024/program/content/170833)

Abstract: We propose Selfrionette, a controller that uses fingertip force input to drive avatar movements in virtual reality (VR). 
This system enables users to interact with virtual objects and walk in VR using only fingertip force, overcoming physical and spatial constraints. Additionally, by fixing users' fingers, it provides users with counterforces equivalent to the applied force, allowing for diverse and wide dynamic range haptic feedback by adjusting the relationship between force input and virtual movement.
To evaluate the effectiveness of the proposed method, this paper focuses on hand interaction as a first step.
In User Study 1, we measured usability and embodiment during reaching tasks under Selfrionette, body tracking, and finger tracking conditions.
In User Study 2, we investigated whether users could perceive haptic properties such as weight, friction, and compliance under the same conditions as User Study 1.
Selfrionette was found to be comparable to body tracking in realism of haptic interaction, enabling embodied avatar experiences even in limited spatial conditions.



### SpinShot: Optimizing Both Physical and Perceived Force Feedback of Flywheel-Based, Directional Impact Handheld Devices
Authors: Chia-An Fan, En-Huei Wu, Chia-Yu Cheng, Yu-Cheng Chang, Alvaro Lopez, Yu Chen, Chia-Chen Chi, Yi-Sheng Chan, Ching-Yi Tsai, Mike Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170972)

Abstract: Real-world impact, such as hitting a tennis ball and a baseball, generates instantaneous, directional impact forces. However, current ungrounded force feedback technologies, such as air jets and propellers, can only generate directional impulses that are 10x-10,000x weaker. We present SpinShot, a flywheel-based device with a solenoid-actuated stopper capable of generating directional impulse of 22Nm in 1ms, which is more than 10x stronger than prior ungrounded directional technologies. Furthermore, we present a novel force design that reverses the flywheel immediately after the initial impact, to significantly increase the perceived magnitude. We conducted a series of two formative, perceptual studies (n=16, 18), followed by a summative user experience study (n=16) that compared SpinShot vs. moving mass (solenoid) and vs. air jets in a VR baseball hitting game. Results showed that SpinShot significantly improved realism, immersion, magnitude (p < .01) compared to both baselines, but significantly reduced comfort vs. air jets primarily due to the 2.9x device weight. Overall, SpinShot was preferred by 63-75% of the participants.




## Vision-based UIs
### Vision-Based Hand Gesture Customization from a Single Demonstration
Authors: Soroush Shahi, Vimal Mollyn, Cori Tymoszek Park, Runchang Kang, Asaf Liberman, Oron Levy, Jun Gong, Abdelkareem Bedri, Gierad Laput

[Link](https://programs.sigchi.org/uist/2024/program/content/170938)

Abstract: Hand gesture recognition is becoming a more prevalent mode of human-computer interaction, especially as cameras proliferate across everyday devices. Despite continued progress in this field, gesture customization is often underexplored. Customization is crucial since it enables users to define and demonstrate gestures that are more natural, memorable, and accessible. However, customization requires efficient usage of user-provided data. We introduce a method that enables users to easily design bespoke gestures with a monocular camera from one demonstration. We employ transformers and meta-learning techniques to address few-shot learning challenges. Unlike prior work, our method supports any combination of one-handed, two-handed, static, and dynamic gestures, including different viewpoints, and the ability to handle irrelevant hand movements. We implement three real-world applications using our customization method, conduct a user study, and achieve up to 94\% average recognition accuracy from one demonstration. Our work provides a viable path for vision-based gesture customization, laying the foundation for future advancements in this domain. 



### VirtualNexus: Enhancing 360-Degree Video AR/VR Collaboration with Environment Cutouts and Virtual Replicas
Authors: Xincheng Huang, Michael Yin, Ziyi Xia, Robert Xiao

[Link](https://programs.sigchi.org/uist/2024/program/content/170877)

Abstract: Asymmetric AR/VR collaboration systems bring a remote VR user to a local AR user’s physical environment, allowing them to communicate and work within a shared virtual/physical space. Such systems often display the remote environment through 3D reconstructions or 360° videos. While 360° cameras stream an environment in higher quality, they lack spatial information, making them less interactable. We present VirtualNexus, an AR/VR collaboration system that enhances 360° video AR/VR collaboration with environment cutouts and virtual replicas. VR users can define cutouts of the remote environment to interact with as a world-in-miniature, and their interactions are synchronized to the local AR perspective. Furthermore, AR users can rapidly scan and share 3D virtual replicas of physical objects using neural rendering. We demonstrated our system’s utility through 3 example applications and evaluated our system in a dyadic usability test. VirtualNexus extends the interaction space of 360° telepresence systems, offering improved physical presence, versatility, and clarity in interactions. 



### Personal Time-Lapse
Authors: Nhan Tran, Ethan Yang, Angelique Taylor, Abe Davis

[Link](https://programs.sigchi.org/uist/2024/program/content/170932)

Abstract: Our bodies are constantly in motion—from the bending of arms and legs to the less conscious movement of breathing, our precise shape and location change constantly. This can make subtler developments (e.g., the growth of hair, or the healing of a wound) difficult to observe. Our work focuses on helping users record and visualize this type of subtle, longer-term change. We present a mobile tool that combines custom 3D tracking with interactive visual feedback and computational imaging to capture personal time-lapse, which approximates longer-term video of the subject (typically, part of the capturing user’s body) under a fixed viewpoint, body pose, and lighting condition. These personal time-lapses offer a powerful and detailed way to track visual changes of the subject over time. We begin with a formative study that examines what makes personal time-lapse so difficult to capture. Building on our findings, we motivate the design of our capture tool, evaluate this design with users, and demonstrate its effectiveness in a variety of challenging examples.



### Chromaticity Gradient Mapping for Interactive Control of Color Contrast in Images and Video
Authors: Ruyu Yan, Jiatian Sun, Abe Davis

[Link](https://programs.sigchi.org/uist/2024/program/content/170867)

Abstract: We present a novel perceptually-motivated interactive tool for using color contrast to enhance details represented in the lightness channel of images and video. Our method lets users adjust the perceived contrast of different details by manipulating local chromaticity while preserving the original lightness of individual pixels. Inspired by the use of similar chromaticity mappings in painting, our tool effectively offers contrast along a user-selected gradient of chromaticities as additional bandwidth for representing and enhancing different details in an image. We provide an interface for our tool that closely resembles the familiar design of tonal contrast curve controls that are available in most professional image editing software. We show that our tool is effective for enhancing the perceived contrast of details without altering lightness in an image and present many examples of effects that can be achieved with our method on both images and video.




## Future of Typing
### OptiBasePen: Mobile Base+Pen Input on Passive Surfaces by Sensing Relative Base Motion Plus Close-Range Pen Position
Authors: Andreas Fender, Mohamed Kari

[Link](https://programs.sigchi.org/uist/2024/program/content/170879)

Abstract: Digital pen input devices based on absolute pen position sensing, such as Wacom Pens, support high-fidelity pen input. However, they require specialized sensing surfaces like drawing tablets, which can have a large desk footprint, constrain the possible input area, and limit mobility. In contrast, digital pens with integrated relative sensing enable mobile use on passive surfaces, but suffer from motion artifacts or require surface contact at all times, deviating from natural pen affordances. We present OptiBasePen, a device for mobile pen input on ordinary surfaces. Our prototype consists of two parts: the "base" on which the hand rests and the pen for fine-grained input. The base features a high-precision mouse sensor to sense its own relative motion, and two infrared image sensors to track the absolute pen tip position within the base's frame of reference. This enables pen input on ordinary surfaces without external cameras while also avoiding drift from pen micro-movements. In this work, we present our prototype as well as the general base+pen concept, which combines relative and absolute sensing.



### Palmrest+: Expanding Laptop Input Space with Shear Force on Palm-Resting Area
Authors: Jisu Yim, Seoyeon Bae, Taejun Kim, Sunbum Kim, Geehyuk Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170781)

Abstract: The palmrest area of laptops has the potential as an additional input space, considering its consistent palm contact during keyboard interaction. We propose Palmrest+, leveraging shear force exerted on the palmrest area. We suggest two input techniques: Palmrest Shortcut, for instant shortcut execution, and Palmrest Joystick, for continuous value input. These allow seamless and subtle input amidst keyboard typing. Evaluation of Palmrest Shortcut against conventional keyboard shortcuts revealed faster performance for applying shear force in unimanual and bimanual-manner with a significant reduction in gaze shifting. Additionally, the assessment of Palmrest Joystick against the laptop touchpad demonstrated comparable performance in selecting one- and two- dimensional targets with low-precision pointing, i.e., for short distances and large target sizes. The maximal hand displacement significantly decreased for both Palmrest Shortcut and Palmrest Joystick compared to conventional methods. These findings verify the feasibility and effectiveness of leveraging the palmrest area as an additional input space on laptops, offering promising enhanced typing-related user interaction experiences.



### TouchInsight: Uncertainty-aware Rapid Touch and Text Input for Mixed Reality from Egocentric Vision
Authors: Paul Streli, Mark Richardson, Fadi Botros, Shugao Ma, Robert Wang, Christian Holz

[Link](https://programs.sigchi.org/uist/2024/program/content/170817)

Abstract: While passive surfaces offer numerous benefits for interaction in mixed reality, reliably detecting touch input solely from head-mounted cameras has been a long-standing challenge. Camera specifics, hand self-occlusion, and rapid movements of both head and fingers introduce considerable uncertainty about the exact location of touch events. Existing methods have thus not been capable of achieving the performance needed for robust interaction.
In this paper, we present a real-time pipeline that detects touch input from all ten fingers on any physical surface, purely based on egocentric hand tracking. Our method TouchInsight comprises a neural network to predict the moment of a touch event, the finger making contact, and the touch location. TouchInsight represents locations through a bivariate Gaussian distribution to account for uncertainties due to sensing inaccuracies, which we resolve through contextual priors to accurately infer intended user input.
We first evaluated our method offline and found that it locates input events with a mean error of 6.3 mm, and accurately detects touch events (F1=0.99) and identifies the finger used (F1=0.96). In an online evaluation, we then demonstrate the effectiveness of our approach for a core application of dexterous touch input: two-handed text entry. In our study, participants typed 37.0 words per minute with an uncorrected error rate of 2.9% on average.



### Can Capacitive Touch Images Enhance Mobile Keyboard Decoding?
Authors: Piyawat Lertvittayakumjorn, Shanqing Cai, Billy Dou, Cedric Ho, Shumin Zhai

[Link](https://programs.sigchi.org/uist/2024/program/content/170719)

Abstract: Capacitive touch sensors capture the two-dimensional spatial profile (referred to as a touch heatmap) of a finger's contact with a mobile touchscreen. However, the research and design of touchscreen mobile keyboards -- one of the most speed and accuracy demanding touch interfaces -- has focused on the location of the touch centroid derived from the touch image heatmap as the input, discarding the rest of the raw spatial signals. In this paper, we investigate whether touch heatmaps can be leveraged to further improve the tap decoding accuracy for mobile touchscreen keyboards. Specifically, we developed and evaluated machine-learning models that interpret user taps by using the centroids and/or the heatmaps as their input and studied the contribution of the heatmaps to model performance. The results show that adding the heatmap into the input feature set led to 21.4% relative reduction of character error rates on average, compared to using the centroid alone. Furthermore, we conducted a live user study with the centroid-based and heatmap-based decoders built into Pixel 6 Pro devices and observed lower error rate, faster typing speed, and higher self-reported satisfaction score based on the heatmap-based decoder than the centroid-based decoder. These findings underline the promise of utilizing touch heatmaps for improving typing experience in mobile keyboards.




## Bodily Signals
### Empower Real-World BCIs with NIRS-X: An Adaptive Learning Framework that Harnesses Unlabeled Brain Signals
Authors: Liang Wang, Jiayan Zhang, Jinyang Liu, Devon McKeon, David Guy Brizan, Giles Blaney, Robert Jacob

[Link](https://programs.sigchi.org/uist/2024/program/content/170939)

Abstract: Brain-Computer Interfaces (BCIs) using functional near-infrared spectroscopy (fNIRS) hold promise for future interactive user interfaces due to their ease of deployment and declining cost. However, they typically require a separate calibration process for each user and task, which can be burdensome. Machine learning helps, but faces a data scarcity problem. Due to inherent inter-user variations in physiological data, it has been typical to create a new annotated training dataset for every new task and user. To reduce dependence on such extensive data collection and labeling, we present an adaptive learning framework, NIRS-X, to harness more easily accessible unlabeled fNIRS data.  NIRS-X includes two key components: NIRSiam and NIRSformer. We use the NIRSiam algorithm to extract generalized brain activity representations from unlabeled fNIRS data obtained from previous users and tasks, and then transfer that knowledge to new users and tasks. In conjunction, we design a neural network, NIRSformer, tailored for capturing both local and global, spatial and temporal relationships in multi-channel fNIRS brain input signals. By using unlabeled data from both a previously released fNIRS2MW visual $n$-back dataset and a newly collected fNIRS2MW audio $n$-back dataset, NIRS-X demonstrates its strong adaptation capability to new users and tasks. Results show comparable or superior performance to supervised methods, making NIRS-X promising for real-world fNIRS-based BCIs.



### Understanding the Effects of Restraining Finger Coactivation in Mid-Air Typing: from a Neuromechanical Perspective
Authors: Hechuan Zhang, Xuewei Liang, Ying Lei, Yanjun Chen, Zhenxuan He, Yu Zhang, Lihan Chen, Hongnan Lin, Teng Han, Feng Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/170941)

Abstract: Typing in mid-air is often perceived as intuitive yet presents challenges due to finger coactivation, a neuromechanical phenomenon that involves involuntary finger movements stemming from the lack of physical constraints. Previous studies were used to examine and address the impacts of finger coactivation using algorithmic approaches. Alternatively, this paper explores the neuromechanical effects of finger coactivation on mid-air typing, aiming to deepen our understanding and provide valuable insights to improve these interactions. We utilized a wearable device that restrains finger coactivation as a prop to conduct two mid-air studies, including a rapid finger-tapping task and a ten-finger typing task. The results revealed that restraining coactivation not only reduced mispresses, which is a classic coactivated error always considered as harm caused by coactivation. Unexpectedly, the reduction of motor control errors and spelling errors, thinking as non-coactivated errors, also be observed.
Additionally, the study evaluated the neural resources involved in motor execution using functional Near Infrared Spectroscopy (fNIRS), which tracked cortical arousal during mid-air typing. The findings demonstrated decreased activation in the primary motor cortex of the left hemisphere when coactivation was restrained, suggesting a diminished motor execution load. This reduction suggests that a portion of neural resources is conserved, which also potentially aligns with perceived lower mental workload and decreased frustration levels.



### What is Affective Touch Made Of? A Soft Capacitive Sensor Array Reveals the Interplay between Shear, Normal Stress and Individuality
Authors: Devyani McLaren, Jian Gao, Xiulun Yin, Rúbia Reis Guerra, Preeti Vyas, Chrys Morton, Xi Laura Cang, Yizhong Chen, Yiyuan Sun, Ying Li, John Madden, Karon MacLean

[Link](https://programs.sigchi.org/uist/2024/program/content/171010)

Abstract: Humans physically express emotion by modulating parameters that register on mammalian skin mechanoreceptors, but are unavailable in current touch-sensing technology. 
Greater sensory richness combined with data on affect-expression composition is a prerequisite to estimating affect from touch, with applications including physical human-robot interaction. To examine shear alongside more easily captured normal stresses, we tailored recent capacitive technology to attain performance suitable for affective touch, creating a flexible, reconfigurable and soft 36-taxel array that detects multitouch normal and 2-dimensional shear at ranges of 1.5kPa-43kPa and $\pm$ 0.3-3.8kPa respectively, wirelessly at ~43Hz (1548 taxels/s). In a deep-learning classification of 9 gestures (N=16), inclusion of shear data improved accuracy to 88\%, compared to 80\% with normal stress data alone, confirming shear stress's expressive centrality. 
Using this rich data, we analyse the interplay of sensed-touch features, gesture attributes and individual differences, propose affective-touch sensing requirements, and share technical considerations for performance and practicality.



### Exploring the Effects of Sensory Conflicts on Cognitive Fatigue in VR Remappings
HONORABLE_MENTION

Authors: Tianren Luo, Gaozhang Chen, Yijian Wen, Pengxiang Wang, yachun fan, Teng Han, Feng Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/171000)

Abstract: Virtual reality (VR) is found to present significant cognitive challenges due to its immersive nature and frequent sensory conflicts. This study systematically investigates the impact of sensory conflicts induced by VR remapping techniques on cognitive fatigue, and unveils their correlation. We utilized three remapping methods (haptic repositioning, head-turning redirection, and giant resizing) to create different types of sensory conflicts, and measured perceptual thresholds to induce various intensities of the conflicts. Through experiments involving cognitive tasks along with subjective and physiological measures, we found that all three remapping methods influenced the onset and severity of cognitive fatigue, with visual-vestibular conflict having the greatest impact. Interestingly, visual-experiential/memory conflict showed a mitigating effect on cognitive fatigue, emphasizing the role of novel sensory experiences. This study contributes to a deeper understanding of cognitive fatigue under sensory conflicts and provides insights for designing VR experiences that align better with human perceptual and cognitive capabilities. 




## Shared Spaces
### BlendScape: Enabling End-User Customization of Video-Conferencing Environments through Generative AI
HONORABLE_MENTION

Authors: Shwetha Rajaram, Nels Numan, Bala Kumaravel, Nicolai Marquardt, Andrew Wilson

[Link](https://programs.sigchi.org/uist/2024/program/content/170854)

Abstract: Today’s video-conferencing tools support a rich range of professional and social activities, but their generic meeting environments cannot be dynamically adapted to align with distributed collaborators’ needs. To enable end-user customization, we developed BlendScape, a rendering and composition system for video-conferencing participants to tailor environments to their meeting context by leveraging AI image generation techniques. BlendScape supports flexible representations of task spaces by blending users’ physical or digital backgrounds into unified environments and implements multimodal interaction techniques to steer the generation. Through an exploratory study with 15 end-users, we investigated whether and how they would find value in using generative AI to customize video-conferencing environments. Participants envisioned using a system like BlendScape to facilitate collaborative activities in the future, but required further controls to mitigate distracting or unrealistic visual elements. We implemented scenarios to demonstrate BlendScape's expressiveness for supporting environment design strategies from prior work and propose composition techniques to improve the quality of environments.



### MyWebstrates: Webstrates as Local-first Software
Authors: Clemens Klokmose, James Eagan, Peter van Hardenberg

[Link](https://programs.sigchi.org/uist/2024/program/content/170812)

Abstract: Webstrates are web substrates, a practical realization of shareable dynamic media under which distributability, shareability, and malleability are fundamental software principles. Webstrates blur the distinction between application and document in a way that enables users to share, repurpose, and refit software across a variety of domains, but its reliance on a central server constrains its use; it is at odds with personal and collective control of data; and limits applications to the web. We extend the fundamental principles to include interoperability and sovereignty over data and propose MyWebstrates, an implementation of Webstrates on top of a new, lower-level substrate for synchronization built around local-first software principles. MyWebstrates registers itself in the user’s browser and function as a piece of local software that can selectively synchronise data over sync servers or peer-to-peer connections. We show how MyWebstrates extends Webstrates to enable offline collaborative use, interoperate between Webstrates on non-web technologies such as Unity, and maintain personal and collective sovereignty over data. We demonstrate how this enables new types of applications of Webstrates and discuss limitations of this approach and new challenges that it reveals.



### SituationAdapt: Contextual UI Optimization in Mixed Reality with Situation Awareness via LLM Reasoning
Authors: Zhipeng Li, Christoph Gebhardt, Yves Inglin, Nicolas Steck, Paul Streli, Christian Holz

[Link](https://programs.sigchi.org/uist/2024/program/content/170856)

Abstract: Mixed Reality is increasingly used in mobile settings beyond controlled home and office spaces. This mobility introduces the need for user interface layouts that adapt to varying contexts. However, existing adaptive systems are designed only for static environments. In this paper, we introduce SituationAdapt, a system that adjusts Mixed Reality UIs to real-world surroundings by considering environmental and social cues in shared settings. Our system consists of perception, reasoning, and optimization modules for UI adaptation. Our perception module identifies objects and individuals around the user, while our reasoning module leverages a Vision-and-Language Model to assess the placement of interactive UI elements. This ensures that adapted layouts do not obstruct relevant environmental cues or interfere with social norms. Our optimization module then generates Mixed Reality interfaces that account for these considerations as well as temporal constraints The evaluation of SituationAdapt is two-fold: We first validate our reasoning component’s capability in assessing UI contexts comparable to human expert users. In an online user study, we then established our system’s capability of producing context-aware MR layouts, where it outperformed adaptive methods from previous work. We further demonstrate the versatility and applicability of SituationAdapt with a set of application scenarios.



### Desk2Desk: Optimization-based Mixed Reality Workspace Integration for Remote Side-by-side Collaboration
Authors: Ludwig Sidenmark, Tianyu Zhang, Leen Al Lababidi, Jiannan Li, Tovi Grossman

[Link](https://programs.sigchi.org/uist/2024/program/content/170830)

Abstract: Mixed Reality enables hybrid workspaces where physical and virtual monitors are adaptively created and moved to suit the current environment and needs. However, in shared settings, individual users’ workspaces are rarely aligned and can vary significantly in the number of monitors, available physical space, and workspace layout, creating inconsistencies between workspaces which may cause confusion and reduce collaboration. We present Desk2Desk, an optimization-based approach for remote collaboration in which the hybrid workspaces of two collaborators are fully integrated to enable immersive side-by-side collaboration. The optimization adjusts each user’s workspace in layout and number of shared monitors and creates a mapping between workspaces to handle inconsistencies between workspaces due to physical constraints (e.g. physical monitors). We show in a user study how our system adaptively merges dissimilar physical workspaces to enable immersive side-by-side collaboration, and demonstrate how an optimization-based approach can effectively address dissimilar physical layouts.




### SpaceBlender: Creating Context-Rich Collaborative Spaces Through Generative 3D Scene Blending
Authors: Nels Numan, Shwetha Rajaram, Bala Kumaravel, Nicolai Marquardt, Andrew Wilson

[Link](https://programs.sigchi.org/uist/2024/program/content/170843)

Abstract: There is increased interest in using generative AI to create 3D spaces for virtual reality (VR) applications. However, today’s models produce artificial environments, falling short of supporting collaborative tasks that benefit from incorporating the user's physical context. To generate environments that support VR telepresence, we introduce SpaceBlender, a novel pipeline that utilizes generative AI techniques to blend users' physical surroundings into unified virtual spaces. This pipeline transforms user-provided 2D images into context-rich 3D environments through an iterative process consisting of depth estimation, mesh alignment, and diffusion-based space completion guided by geometric priors and adaptive text prompts. In a preliminary within-subjects study, where 20 participants performed a collaborative VR affinity diagramming task in pairs, we compared SpaceBlender with a generic virtual environment and a state-of-the-art scene generation framework, evaluating its ability to create virtual spaces suitable for collaboration. Participants appreciated the enhanced familiarity and context provided by SpaceBlender but also noted complexities in the generative environments that could detract from task focus. Drawing on participant feedback, we propose directions for improving the pipeline and discuss the value and design of blended spaces for different scenarios.




## AI & Automation
### Memolet: Reifying the Reuse of User-AI Conversational Memories
Authors: Ryan Yen, Jian Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/170751)

Abstract: As users engage more frequently with AI conversational agents, conversations may exceed their memory capacity, leading to failures in correctly leveraging certain memories for tailored responses. However, in finding past memories that can be reused or referenced, users need to retrieve relevant information in various conversations and articulate to the AI their intention to reuse these memories. To support this process, we introduce Memolet, an interactive object that reifies memory reuse. Users can directly manipulate Memolet to specify which memories to reuse and how to use them. We developed a system demonstrating Memolet's interaction across various memory reuse stages, including memory extraction, organization, prompt articulation, and generation refinement. We examine the system's usefulness with an N=12 within-subject study and provide design implications for future systems that support user-AI conversational memory reusing.



### VIME: Visual Interactive Model Explorer for Identifying Capabilities and Limitations of Machine Learning Models for Sequential Decision-Making
Authors: Anindya Das Antar, Somayeh Molaei, Yan-Ying Chen, Matthew Lee, Nikola Banovic

[Link](https://programs.sigchi.org/uist/2024/program/content/170861)

Abstract: Ensuring that Machine Learning (ML) models make correct and meaningful inferences is necessary for the broader adoption of such models into high-stakes decision-making scenarios. Thus, ML model engineers increasingly use eXplainable AI (XAI) tools to investigate the capabilities and limitations of their ML models before deployment. However, explaining sequential ML models, which make a series of decisions at each timestep, remains challenging. We present Visual Interactive Model Explorer (VIME), an XAI toolbox that enables ML model engineers to explain decisions of sequential models in different ``what-if'' scenarios. Our evaluation with 14 ML experts, who investigated two existing sequential ML models using VIME and a baseline XAI toolbox to explore ``what-if'' scenarios, showed that VIME made it easier to identify and explain instances when the models made wrong decisions compared to the baseline. Our work informs the design of future interactive XAI mechanisms for evaluating sequential ML-based decision support systems.



### SERENUS: Alleviating Low-Battery Anxiety Through Real-time, Accurate, and User-Friendly Energy Consumption Prediction of Mobile Applications
Authors: Sera Lee, Dae R. Jeong, Junyoung Choi, Jaeheon Kwak, Seoyun Son, Jean Song, Insik Shin

[Link](https://programs.sigchi.org/uist/2024/program/content/170937)

Abstract: Low-battery anxiety has emerged as a result of growing dependence on mobile devices, where the anxiety arises when the battery level runs low. While battery life can be extended through power-efficient hardware and software optimization techniques, low-battery anxiety will remain a phenomenon as long as mobile devices rely on batteries. In this paper, we investigate how an accurate real-time energy consumption prediction at the application-level can improve the user experience in low-battery situations. We present Serenus, a mobile system framework specifically tailored to predict the energy consumption of each mobile application and present the prediction in a user-friendly manner. We conducted user studies using Serenus to verify that highly accurate energy consumption predictions can effectively alleviate low-battery anxiety by assisting users in planning their application usage based on the remaining battery life. We summarize requirements to mitigate users’ anxiety, guiding the design of future mobile system frameworks.




## Poses as Input
### SolePoser: Real-Time 3D Human Pose Estimation using Insole Pressure Sensors
Authors: Erwin Wu, Rawal Khirodkar, Hideki Koike, Kris Kitani

[Link](https://programs.sigchi.org/uist/2024/program/content/170905)

Abstract: We propose SolePoser, a real-time 3D pose estimation system that leverages only a single pair of insole sensors. Unlike conventional methods relying on fixed cameras or bulky wearable sensors, our approach offers minimal and natural setup requirements. The proposed system utilizes pressure and IMU sensors embedded in insoles to capture the body weight's pressure distribution at the feet and its 6 DoF acceleration. This information is used to estimate the 3D full-body joint position by a two-stream transformer network. A novel double-cycle consistency loss and a cross-attention module are further introduced to learn the relationship between 3D foot positions and their pressure distributions.
We also introduced two different datasets of sports and daily exercises, offering 908k frames across eight different activities. Our experiments show that our method's performance is on par with top-performing approaches, which utilize more IMUs and even outperform third-person-view camera-based methods in certain scenarios. 



### Gait Gestures: Examining Stride and Foot Strike Variation as an Input Method While Walking
Authors: Ching-Yi Tsai, Ryan Yen, Daekun Kim, Daniel Vogel

[Link](https://programs.sigchi.org/uist/2024/program/content/170926)

Abstract: Walking is a cyclic pattern of alternating footstep strikes, with each pair of steps forming a stride, and a series of strides forming a gait.  We conduct a systematic examination of different kinds of intentional variations from a normal gait that could be used as input actions without interrupting overall walking progress. A design space of 22 candidate Gait Gestures is generated by adapting previous standing foot input actions and identifying new actions possible in a walking context.  A formative study (n=25) examines movement easiness, social acceptability, and walking compatibility with foot movement logging to calculate temporal and spatial characteristics. Using a categorization of these results, 7 gestures are selected for a wizard-of-oz prototype demonstrating an AR interface controlled by Gait Gestures for ordering food and audio playback while walking. As a technical proof-of-concept, a gait gesture recognizer is developed and tested using the formative study data.



### EgoTouch: On-Body Touch Input Using AR/VR Headset Cameras
Authors: Vimal Mollyn, Chris Harrison

[Link](https://programs.sigchi.org/uist/2024/program/content/170875)

Abstract: In augmented and virtual reality (AR/VR) experiences, a user’s arms and hands can provide a convenient and tactile surface for touch input. Prior work has shown on-body input to have significant speed, accuracy, and ergonomic benefits over in-air interfaces, which are common today. In this work, we demonstrate high accuracy, bare hands (i.e., no special instrumentation of the user) skin input using just an RGB camera, like those already integrated into all modern XR headsets. Our results show this approach can be accurate, and robust across diverse lighting conditions, skin tones, and body motion (e.g., input while walking). Finally, our pipeline also provides rich input metadata including touch force, finger identification, angle of attack, and rotation. We believe these are the requisite technical ingredients to more fully unlock on-skin interfaces that have been well motivated in the HCI literature but have lacked robust and practical methods.



### MobilePoser: Real-Time Full-Body Pose Estimation and 3D Human Translation from IMUs in Mobile Consumer Devices
Authors: Vasco Xu, Chenfeng Gao, Henry Hoffman, Karan Ahuja

[Link](https://programs.sigchi.org/uist/2024/program/content/170732)

Abstract: There has been a continued trend towards minimizing instrumentation for full-body motion capture, going from specialized rooms and equipment, to arrays of worn sensors and recently sparse inertial pose capture methods. However, as these techniques migrate towards lower-fidelity IMUs on ubiquitous commodity devices, like phones, watches, and earbuds, challenges arise including compromised online performance, temporal consistency, and loss of global translation due to sensor noise and drift. Addressing these challenges, we introduce MobilePoser, a real-time system for full-body pose and global translation estimation using any available subset of IMUs already present in these consumer devices. MobilePoser employs a multi-stage deep neural network for kinematic pose estimation followed by a physics-based motion optimizer, achieving state-of-the-art accuracy while remaining lightweight. We conclude with a series of demonstrative applications to illustrate the unique potential of MobilePoser across a variety of fields, such as health and wellness, gaming, and indoor navigation to name a few.  



### Touchscreen-based Hand Tracking for Remote Whiteboard Interaction
Authors: Xinshuang Liu, Yizhong Zhang, Xin Tong

[Link](https://programs.sigchi.org/uist/2024/program/content/170956)

Abstract: In whiteboard-based remote communication, the seamless integration of drawn content and hand-screen interactions is essential for an immersive user experience. Previous methods either require bulky device setups for capturing hand gestures or fail to accurately track the hand poses from capacitive images. In this paper, we present a real-time method for precise tracking 3D poses of both hands from capacitive video frames. To this end, we develop a deep neural network to identify hands and infer hand joint positions from capacitive frames, and then recover 3D hand poses from the hand-joint positions via a constrained inverse kinematic solver. Additionally, we design a device setup for capturing high-quality hand-screen interaction data and obtained a more accurate synchronized capacitive video and hand pose dataset. Our method improves the accuracy and stability of 3D hand tracking for capacitive frames while maintaining a compact device setup for remote communication. We validate our scheme design and its superior performance on 3D hand pose tracking and demonstrate the effectiveness of our method in whiteboard-based remote communication. 



### SeamPose: Repurposing Seams as Capacitive Sensors in a Shirt for Upper-Body Pose Tracking
Authors: Tianhong Yu, Mary Zhang, Peter He, Chi-Jung Lee, Cassidy Cheesman, Saif Mahmud, Ruidong Zhang, Francois Guimbretiere, Cheng Zhang

[Link](https://programs.sigchi.org/uist/2024/program/content/170739)

Abstract: Seams are areas of overlapping fabric formed by stitching two or more pieces of fabric together in the cut-and-sew apparel manufacturing process. In SeamPose, we repurposed seams as capacitive sensors in a shirt for continuous upper-body pose estimation. Compared to previous all-textile motion-capturing garments that place the electrodes on the clothing surface, our solution leverages existing seams inside of a shirt by machine-sewing insulated conductive threads over the seams. The unique invisibilities and placements of the seams afford the sensing shirt to look and wear similarly as a conventional shirt while providing exciting pose-tracking capabilities. To validate this approach, we implemented a proof-of-concept untethered shirt with 8 capacitive sensing seams. With a 12-participant user study, our customized deep-learning pipeline accurately estimates the relative (to the pelvis) upper-body 3D joint positions with a mean per joint position error (MPJPE) of 6.0 cm. SeamPose represents a step towards unobtrusive integration of smart clothing for everyday pose estimation.




## AI as Copilot
### DiscipLink: Unfolding Interdisciplinary Information Seeking Process via Human-AI Co-Exploration
Authors: Chengbo Zheng, Yuanhao Zhang, Zeyu Huang, Chuhan Shi, Minrui Xu, Xiaojuan Ma

[Link](https://programs.sigchi.org/uist/2024/program/content/170741)

Abstract: Interdisciplinary studies often require researchers to explore literature in diverse branches of knowledge. Yet, navigating through the highly scattered knowledge from unfamiliar disciplines poses a significant challenge. In this paper, we introduce DiscipLink, a novel interactive system that facilitates collaboration between researchers and large language models (LLMs) in interdisciplinary information seeking (IIS). Based on users' topic of interest, DiscipLink initiates exploratory questions from the perspectives of possible relevant fields of study, and users can further tailor these questions. DiscipLink then supports users in searching and screening papers under selected questions by automatically expanding queries with disciplinary-specific terminologies, extracting themes from retrieved papers, and highlighting the connections between papers and questions. Our evaluation, comprising a within-subject comparative experiment and an open-ended exploratory study, reveals that DiscipLink can effectively support researchers in breaking down disciplinary boundaries and integrating scattered knowledge in diverse fields. The findings underscore the potential of LLM-powered tools in fostering information-seeking practices and bolstering interdisciplinary research.



### Improving Steering and Verification in AI-Assisted Data Analysis with Interactive Task Decomposition
Authors: Majeed Kazemitabaar, Jack Williams, Ian Drosos, Tovi Grossman, Austin Henley, Carina Negreanu, Advait Sarkar

[Link](https://programs.sigchi.org/uist/2024/program/content/170918)

Abstract: LLM-powered tools like ChatGPT Data Analysis, have the potential to help users tackle the challenging task of data analysis programming, which requires expertise in data processing, programming, and statistics. However, our formative study (n=15) uncovered serious challenges in verifying AI-generated results and steering the AI (i.e., guiding the AI system to produce the desired output). We developed two contrasting approaches to address these challenges. The first (Stepwise) decomposes the problem into step-by-step subgoals with pairs of editable assumptions and code until task completion, while the second (Phasewise) decomposes the entire problem into three editable, logical phases: structured input/output assumptions, execution plan, and code. A controlled, within-subjects experiment (n=18) compared these systems against a conversational baseline. Users reported significantly greater control with the Stepwise and Phasewise systems, and found intervention, correction, and verification easier, compared to the baseline. The results suggest design guidelines and trade-offs for AI-assisted data analysis tools.




### VizGroup: An AI-assisted Event-driven System for Collaborative Programming Learning Analytics
Authors: Xiaohang Tang, Sam Wong, Kevin Pu, Xi Chen, Yalong Yang, Yan Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170725)

Abstract: Programming instructors often conduct collaborative learning activities, like Peer Instruction, to foster a deeper understanding in students and enhance their engagement with learning. These activities, however, may not always yield productive outcomes due to the diversity of student mental models and their ineffective collaboration. In this work, we introduce VizGroup, an AI-assisted system that enables programming instructors to easily oversee students' real-time collaborative learning behaviors during large programming courses. VizGroup leverages Large Language Models (LLMs) to recommend event specifications for instructors so that they can simultaneously track and receive alerts about key correlation patterns between various collaboration metrics and ongoing coding tasks. We evaluated VizGroup with 12 instructors in a comparison study using a dataset collected from a Peer Instruction activity that was conducted in a large programming lecture. 
The results showed that VizGroup helped instructors effectively overview, narrow down, and track nuances throughout students' behaviors.



### Who did it? How User Agency is influenced by Visual Properties of Generated Images
Authors: Johanna Didion, Krzysztof Wolski, Dennis Wittchen, David Coyle, Thomas Leimkühler, Paul Strohmeier

[Link](https://programs.sigchi.org/uist/2024/program/content/170827)

Abstract: The increasing proliferation of AI and GenAI requires new interfaces tailored to how their specific affordances and human requirements meet. As GenAI is capable of taking over tasks from users on an unprecedented scale, designing the experience of agency -- if and how users experience control over the process and responsibility over the outcome -- is crucial. As an initial step towards design guidelines for shaping agency, we present a study that explores how features of AI-generated images influence users' experience of agency. We use two measures; temporal binding to implicitly estimate pre-reflective agency and magnitude estimation to assess user judgments of agency. We observe that abstract images lead to more temporal binding than images with semantic meaning. In contrast, the closer an image aligns with what a user might expect, the higher the agency judgment. When comparing the experiment results with objective metrics of image differences, we find that temporal binding results correlate with semantic differences, while agency judgments are better explained by local differences between images. This work contributes towards a future where agency is considered an important design dimension for GenAI interfaces.



### FathomGPT: A Natural Language Interface for Interactively Exploring Ocean Science Data
Authors: Nabin Khanal, Chun Meng Yu, Jui-Cheng Chiu, Anav Chaudhary, Ziyue Zhang, Kakani Katija, Angus Forbes

[Link](https://programs.sigchi.org/uist/2024/program/content/171001)

Abstract: We introduce FathomGPT, an open source system for the interactive investigation of ocean science data via a natural language interface. FathomGPT was developed in close collaboration with marine scientists to enable researchers and ocean enthusiasts to explore and analyze the FathomNet image database. FathomGPT provides a custom information retrieval pipeline that leverages OpenAI’s large language models to enable: the creation of complex queries to retrieve images, taxonomic information, and scientific measurements; mapping common names and morphological features to scientific names; generating interactive charts on demand; and searching by image or specified patterns within an image. In designing FathomGPT, particular emphasis was placed on enhancing the user's experience by facilitating free-form exploration and optimizing response times. We present an architectural overview and implementation details of  FathomGPT, along with a series of ablation studies that demonstrate the effectiveness of our approach to name resolution, fine tuning, and prompt modification. Additionally, we present usage scenarios of interactive data exploration sessions and document feedback from ocean scientists and machine learning experts.



### VRCopilot: Authoring 3D Layouts with Generative AI Models in VR
Authors: Lei Zhang, Jin Pan, Jacob Gettig, Steve Oney, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170933)

Abstract: Immersive authoring provides an intuitive medium for users to create 3D scenes via direct manipulation in Virtual Reality (VR). Recent advances in generative AI have enabled the automatic creation of realistic 3D layouts. However, it is unclear how capabilities of generative AI can be used in immersive authoring to support fluid interactions, user agency, and creativity. We introduce VRCopilot, a mixed-initiative system that integrates pre-trained generative AI models into immersive authoring to facilitate human-AI co-creation in VR. VRCopilot presents multimodal interactions to support rapid prototyping and iterations with AI, and intermediate representations such as wireframes to augment user controllability over the created content. Through a series of user studies, we evaluated the potential and challenges in manual, scaffolded, and automatic creation in immersive authoring. We found that scaffolded creation using wireframes enhanced the user agency compared to automatic creation. We also found that manual creation via multimodal specification offers the highest sense of creativity and agency.




## Body as the interface
### MouthIO: Fabricating Customizable Oral User Interfaces with Integrated Sensing and Actuation
Authors: Yijing Jiang, Julia Kleinau, Till Max Eckroth, Eve Hoggan, Stefanie Mueller, Michael Wessely

[Link](https://programs.sigchi.org/uist/2024/program/content/170798)

Abstract: This paper introduces MouthIO, the first customizable intraoral user interface that can be equipped with various sensors and output components. MouthIO consists of an SLA-printed brace that houses a flexible PCB within a bite-proof enclosure positioned between the molar teeth and inner cheeks. Our MouthIO design and fabrication technique enables makers to customize the oral user interfaces in both form and function at low cost. All parts in contact with the oral cavity are made of bio-compatible materials to ensure safety, while the design takes into account both comfort and portability. We demonstrate MouthIO through three application examples ranging from beverage consumption monitoring, health monitoring, to assistive technology. Results from our full-day user study indicate high wearability and social acceptance levels, while our technical evaluation demonstrates the device's ability to withstand adult bite forces.



### Can a Smartwatch Move Your Fingers? Compact and Practical Electrical Muscle Stimulation in a Smartwatch
HONORABLE_MENTION

Authors: Akifumi Takahashi, Yudai Tanaka, Archit Tamhane, Alan Shen, Shan-Yuan Teng, Pedro Lopes

[Link](https://programs.sigchi.org/uist/2024/program/content/170990)

Abstract: Smartwatches gained popularity in the mainstream, making them into today’s de-facto wearables. Despite advancements in sensing, haptics on smartwatches is still restricted to tactile feedback (e.g., vibration). Most smartwatch-sized actuators cannot render strong force-feedback. Simultaneously, electrical muscle stimulation (EMS) promises compact force-feedback but, to actuate fingers requires users to wear many electrodes on their forearms. While forearm electrodes provide good accuracy, they detract EMS from being a practical force-feedback interface. To address this, we propose moving the electrodes to the wrist—conveniently packing them in the backside of a smartwatch. In our first study, we found that by cross-sectionally stimulating the wrist in 1,728 trials, we can actuate thumb extension, index extension & flexion, middle flexion, pinky flexion, and wrist flexion. Following, we engineered a compact EMS that integrates directly into a smartwatch’s wristband (with a custom stimulator, electrodes, demultiplexers, and communication). In our second study, we found that participants could calibrate our device by themselves ~50% faster than with conventional EMS. Furthermore, all participants preferred the experience of this device, especially for its social acceptability & practicality. We believe that our approach opens new applications for smartwatch-based interactions, such as haptic assistance during everyday tasks.



### Power-over-Skin: Full-Body Wearables Powered By Intra-Body RF Energy
Authors: Andy Kong, Daehwa Kim, Chris Harrison

[Link](https://programs.sigchi.org/uist/2024/program/content/170775)

Abstract: Powerful computing devices are now small enough to be easily worn on the body. However, batteries pose a major design and user experience obstacle, adding weight and volume, and generally requiring periodic device removal and recharging. In response, we developed Power-over-Skin, an approach using the human body itself to deliver power to many distributed, battery-free, worn devices. We demonstrate power delivery from on-body distances as far as from head-to-toe, with sufficient energy to power microcontrollers capable of sensing and wireless communication. We share results from a study campaign that informed our implementation, as well as experiments that validate our final system. We conclude with several demonstration devices, ranging from input controllers to longitudinal bio-sensors, which highlight the efficacy and potential of our approach.



### HandPad: Make Your Hand an On-the-go Writing Pad via Human Capacitance
Authors: Yu Lu, Dian Ding, Hao Pan, Yijie Li, Juntao Zhou, Yongjian Fu, Yongzhao Zhang, Yi-Chao Chen, Guangtao Xue

[Link](https://programs.sigchi.org/uist/2024/program/content/170761)

Abstract: The convenient text input system is a pain point for devices such as AR glasses, and it is difficult for existing solutions to balance portability and efficiency. This paper introduces HandPad, the system that turns the hand into an on-the-go touchscreen, which realizes interaction on the hand via human capacitance. HandPad achieves keystroke and handwriting inputs for letters, numbers, and Chinese characters, reducing the dependency on capacitive or pressure sensor arrays. Specifically, the system verifies the feasibility of touch point localization on the hand using the human capacitance model and proposes a handwriting recognition system based on Bi-LSTM and ResNet. The transfer learning-based system only needs a small amount of training data to build a handwriting recognition model for the target user. Experiments in real environments verify the feasibility of HandPad for keystroke (accuracy of 100%) and handwriting recognition for letters (accuracy of 99.1%), numbers (accuracy of 97.6%) and Chinese characters (accuracy of 97.9%).




## New Vizualizations
### VisCourt: In-Situ Guidance for Interactive Tactic Training in Mixed Reality
Authors: Liqi Cheng, Hanze Jia, Lingyun Yu, Yihong Wu, Shuainan Ye, Dazhen Deng, Hui Zhang, Xiao Xie, Yingcai Wu

[Link](https://programs.sigchi.org/uist/2024/program/content/170791)

Abstract: In team sports like basketball, understanding and executing tactics---coordinated plans of movements among players---are crucial yet complex, requiring extensive practice. These tactics require players to develop a keen sense of spatial and situational awareness. Traditional coaching methods, which mainly rely on basketball tactic boards and video instruction, often fail to bridge the gap between theoretical learning and the real-world application of tactics, due to shifts in view perspectives and a lack of direct experience with tactical scenarios. To address this challenge, we introduce VisCourt, a Mixed Reality (MR) tactic training system, in collaboration with a professional basketball team. To set up the MR training environment, we employed semi-automatic methods to simulate realistic 3D tactical scenarios and iteratively designed visual in-situ guidance. This approach enables full-body engagement in interactive training sessions on an actual basketball court and provides immediate feedback, significantly enhancing the learning experience. A user study with athletes and enthusiasts shows the effectiveness and satisfaction with VisCourt in basketball training and offers insights for the design of future SportsXR training systems.



### Block and Detail: Scaffolding Sketch-to-Image Generation
Authors: Vishnu Sarukkai, Lu Yuan, Mia Tang, Maneesh Agrawala, Kayvon Fatahalian

[Link](https://programs.sigchi.org/uist/2024/program/content/170911)

Abstract: We introduce a novel sketch-to-image tool that aligns with the iterative refinement process of artists. Our tool lets users sketch blocking strokes to coarsely represent the placement and form of objects and detail strokes to refine their shape and silhouettes. We develop a two-pass algorithm for generating high-fidelity images from such sketches at any point in the iterative process. In the first pass we use a ControlNet to generate an image that strictly follows all the strokes (blocking and detail) and in the second pass we add variation by renoising regions surrounding blocking strokes. We also present a dataset generation scheme that, when used to train a ControlNet architecture, allows regions that do not contain strokes to be interpreted as not-yet-specified regions rather than empty space. We show that this partial-sketch-aware ControlNet can generate coherent elements from partial sketches that only contain a small number of strokes. The high-fidelity images produced by our approach serve as scaffolds that can help the user adjust the shape and proportions of objects or add additional elements to the composition. We demonstrate the effectiveness of our approach with a variety of examples and evaluative comparisons. Quantitatively, novice viewers prefer the quality of images from our algorithm over a baseline Scribble ControlNet for 82% of the pairs and found our images had less distortion in 80% of the pairs.



### EVE: Enabling Anyone to Train Robots using Augmented Reality
Authors: Jun Wang, Chun-Cheng Chang, Jiafei Duan, Dieter Fox, Ranjay Krishna

[Link](https://programs.sigchi.org/uist/2024/program/content/170803)

Abstract: The increasing affordability of robot hardware is accelerating the integration of robots into everyday activities. However, training a robot to automate a task requires expensive trajectory data where a trained human annotator moves a physical robot to train it. Consequently, only those with access to robots produce demonstrations to train robots. In this work, we remove this restriction with EVE, an iOS app that enables everyday users to train robots using intuitive augmented reality visualizations, without needing a physical robot. With EVE, users can collect demonstrations by specifying waypoints with their hands, visually inspecting the environment for obstacles, modifying existing waypoints, and verifying collected trajectories. In a user study (N=14, D=30) consisting of three common tabletop tasks, EVE outperformed three state-of-the-art interfaces in success rate and was comparable to kinesthetic teaching—physically moving a physical robot—in completion time, usability, motion intent communication, enjoyment, and preference (mean of p=0.30). EVE allows users to train robots for personalized tasks, such as sorting desk supplies, organizing ingredients, or setting up board games. We conclude by enumerating limitations and design considerations for future AR-based demonstration collection systems for robotics.



### avaTTAR: Table Tennis Stroke Training with On-body and Detached Visualization in Augmented Reality
Authors: Dizhi Ma, Xiyun Hu, Jingyu Shi, Mayank Patel, Rahul Jain, Ziyi Liu, Zhengzhe Zhu, Karthik Ramani

[Link](https://programs.sigchi.org/uist/2024/program/content/170894)

Abstract: Table tennis stroke training is a critical aspect of player development. We designed a new augmented reality (AR) system, avaTTAR, for table tennis stroke training. The system provides both “on-body” (first-person view) and “detached” (third-person view)
visual cues, enabling users to visualize target strokes and correct their attempts effectively with this dual perspectives setup. By employing a combination of pose estimation algorithms and IMU sensors, avaTTAR captures and reconstructs the 3D body pose and paddle orientation of users during practice, allowing real-time comparison with expert strokes. Through a user study, we affirm avaTTAR ’s capacity to amplify player experience and training results




## Big to Small Fab
### Don't Mesh Around: Streamlining Manual-Digital Fabrication Workflows with Domain-Specific 3D Scanning
Authors: Ilan Moyer, Sam Bourgault, Devon Frost, Jennifer Jacobs

[Link](https://programs.sigchi.org/uist/2024/program/content/170846)

Abstract: Software-first digital fabrication workflows are often at odds with material-driven approaches to design. Material-driven design is especially critical in manual ceramics, where the craftsperson shapes the form through hands-on engagement. We present the Craft-Aligned Scanner (CAS), a 3D scanning and clay-3D printing system that enables practitioners to design for digital fabrication through traditional pottery techniques. The CAS augments a pottery wheel that has 3D printing capabilities with a precision distance sensor on a vertically oriented linear axis. By increasing the height of the sensor as the wheel turns, we directly synthesize a 3D spiralized toolpath from the geometry of the object on the wheel, enabling the craftsperson to immediately transition from manual fabrication to 3D printing without leaving the tool. We develop new digital fabrication workflows with CAS to augment scanned forms with functional features and add both procedurally and real-time-generated surface textures. CAS demonstrates how 3D printers can support material-first digital fabrication design without foregoing the expressive possibilities of software-based design.



### E-Joint: Fabrication of Large-Scale Interactive Objects Assembled by 3D Printed Conductive Parts with Copper Plated Joints
Authors: Xiaolong Li, Cheng Yao, Shang Shi, Shuyue Feng, Yujie Zhou, Haoye Dong, Shichao Huang, Xueyan Cai, Kecheng Jin, Fangtian Ying, Guanyun Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170987)

Abstract: The advent of conductive thermoplastic filaments and multi-material 3D printing has made it feasible to create interactive 3D printed objects. Yet, challenges arise due to volume constraints of desktop 3D printers and high resistive characteristics of current conductive materials, making the fabrication of large-scale or highly conductive interactive objects can be daunting. We propose E-Joint, a novel fabrication pipeline for 3D printed objects utilizing mortise and tenon joint structures combined with a copper plating process. The segmented pieces and joint structures are customized in software along with integrated circuits. Then electroplate them for enhanced conductivity. We designed four distinct electrified joint structures in experiment and evaluated the practical feasibility and effectiveness of fabricating pipes. By constructing three applications with those structures, we verified the usability of E-Joint in making large-scale interactive objects and show path to a more integrated future for manufacturing.



### MobiPrint: A Mobile 3D Printer for Environment-Scale Design and Fabrication
Authors: Daniel Campos Zamora, Liang He, Jon Froehlich

[Link](https://programs.sigchi.org/uist/2024/program/content/170934)

Abstract: 3D printing is transforming how we customize and create physical objects in engineering, accessibility, and art. However, this technology is still primarily limited to confined working areas and dedicated print beds thereby detaching design and fabrication from real-world environments and making measuring and scaling objects tedious and labor-intensive. In this paper, we present MobiPrint, a prototype mobile fabrication system that combines elements from robotics, architecture, and Human-Computer Interaction (HCI) to enable environment-scale design and fabrication in ad-hoc indoor environments. MobiPrint provides a multi-stage fabrication pipeline: first, the robotic 3D printer automatically scans and maps an indoor space; second, a custom design tool converts the map into an interactive CAD canvas for editing and placing models in the physical world; finally, the MobiPrint robot prints the object directly on the ground at the defined location. Through a "proof-by-demonstration" validation, we highlight our system's potential across different applications, including accessibility, home furnishing, floor signage, and art. We also conduct a technical evaluation to assess MobiPrint’s localization accuracy, ground surface adhesion, payload capacity, and mapping speed. We close with a discussion of open challenges and opportunities for the future of contextualized mobile fabrication.



### StructCurves: Interlocking Block-Based Line Structures
Authors: Zezhou Sun, Devin Balkcom, Emily Whiting

[Link](https://programs.sigchi.org/uist/2024/program/content/171006)

Abstract: We present a new class of curved block-based line structures whose component chains are flexible when separated, and provably rigid when assembled together into an interlocking double chain. The joints are inspired by traditional zippers, where a binding fabric or mesh connects individual teeth.
Unlike traditional zippers, the joint design produces a rigid interlock with programmable curvature. This allows fairly strong curved structures to be built out of easily stored flexible chains. 
In this paper, we introduce a pipeline for generating these curved structures using a novel block design template based on revolute joints. 
Mesh embedded in these structures maintains block spacing and assembly order. We evaluate the rigidity of the curved structures through mechanical performance testing and demonstrate several applications. 




## Machine Learning for User Interfaces
### UIClip: A Data-driven Model for Assessing User Interface Design
Authors: Jason Wu, Yi-Hao Peng, Xin Yue Li, Amanda Swearngin, Jeffrey Bigham, Jeffrey Nichols

[Link](https://programs.sigchi.org/uist/2024/program/content/170950)

Abstract: User interface (UI) design is a difficult yet important task for ensuring the usability, accessibility, and aesthetic qualities of applications. In our paper, we develop a machine-learned model, UIClip, for assessing the design quality and visual relevance of a UI given its screenshot and natural language description. To train UIClip, we used a combination of automated crawling, synthetic augmentation, and human ratings to construct a large-scale dataset of UIs, collated by description and ranked by design quality. Through training on the dataset, UIClip implicitly learns properties of good and bad designs by (i) assigning a numerical score that represents a UI design's relevance and quality and (ii) providing design suggestions. In an evaluation that compared the outputs of UIClip and other baselines to UIs rated by 12 human designers, we found that UIClip achieved the highest agreement with ground-truth rankings. Finally, we present three example applications that demonstrate how UIClip can facilitate downstream applications that rely on instantaneous assessment of UI design quality: (i) UI code generation, (ii) UI design tips generation, and (iii) quality-aware UI example search.



### UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset
Authors: Peitong Duan, Chin-Yi Cheng, Gang Li, Bjoern Hartmann, Yang Li

[Link](https://programs.sigchi.org/uist/2024/program/content/170823)

Abstract: Automated UI evaluation can be beneficial for the design process; for example, to compare different UI designs, or conduct automated heuristic evaluation. LLM-based UI evaluation, in particular, holds the promise of generalizability to a wide variety of UI types and evaluation tasks. However, current LLM-based techniques do not yet match the performance of human evaluators. We hypothesize that automatic evaluation can be improved by collecting a targeted UI feedback dataset and then using this dataset to enhance the performance of general-purpose LLMs. We present a targeted dataset of 3,059 design critiques and quality ratings for 983 mobile UIs, collected from seven designers, each with at least a year of professional design experience. We carried out an in-depth analysis to characterize the dataset's features. We then applied this dataset to achieve a 55\% performance gain in LLM-generated UI feedback via various few-shot and visual prompting techniques. We also discuss future applications of this dataset, including training a reward model for generative UI techniques, and fine-tuning a tool-agnostic multi-modal LLM that automates UI evaluation.



### EyeFormer: Predicting Personalized Scanpaths with Transformer-Guided Reinforcement Learning
Authors: Yue Jiang, Zixin Guo, Hamed Rezazadegan Tavakoli, Luis Leiva, Antti Oulasvirta

[Link](https://programs.sigchi.org/uist/2024/program/content/170925)

Abstract: From a visual-perception perspective, modern graphical user interfaces (GUIs) comprise a complex graphics-rich two-dimensional visuospatial arrangement of text, images, and interactive objects such as buttons and menus. While existing models can accurately predict regions and objects that are likely to attract attention ``on average'', no scanpath model has been capable of predicting scanpaths for an individual. To close this gap, we introduce EyeFormer, which utilizes a Transformer architecture as a policy network to guide a deep reinforcement learning algorithm that predicts gaze locations. Our model offers the unique capability of producing personalized predictions when given a few user scanpath samples. It can predict full scanpath information, including fixation positions and durations, across individuals and various stimulus types. Additionally, we demonstrate applications in GUI layout optimization driven by our model. 



### GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning
Authors: Minh Duc Vu, Han Wang, Jieshan Chen, Zhuang Li, Shengdong Zhao, Zhenchang Xing, Chunyang Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170994)

Abstract: Virtual assistants have the potential to play an important role in helping users achieve different tasks. However, these systems face challenges in their real-world usability, characterized by inefficiency and struggles in grasping user intentions. Leveraging recent advances in Large Language Models (LLMs), we introduce GPTVoiceTasker, a virtual assistant poised to enhance user experiences and task efficiency on mobile devices. GPTVoiceTasker excels at intelligently deciphering user commands and executing relevant device interactions to streamline task completion. For unprecedented tasks, GPTVoiceTasker utilises the contextual information and on-screen content to continuously explore and execute the tasks. In addition, the system continually learns from historical user commands to automate subsequent task invocations, further enhancing execution efficiency. From our experiments, GPTVoiceTasker achieved 84.5% accuracy in parsing human commands into executable actions and 85.7% accuracy in automating multi-step tasks. In our user study, GPTVoiceTasker boosted task efficiency in real-world scenarios by 34.85%, accompanied by positive participant feedback. We made GPTVoiceTasker open-source, inviting further research into LLMs utilization for diverse tasks through prompt engineering and leveraging user usage data to improve efficiency.



### VisionTasker: Mobile Task Automation Using Vision Based UI Understanding and LLM Task Planning
Authors: Yunpeng Song, Yiheng Bian, Yongtao Tang, Guiyu Ma, Zhongmin Cai

[Link](https://programs.sigchi.org/uist/2024/program/content/170816)

Abstract: Mobile task automation is an emerging field that leverages AI to streamline and optimize the execution of routine tasks on mobile devices, thereby enhancing efficiency and productivity. Traditional methods, such as Programming By Demonstration (PBD), are limited due to their dependence on predefined tasks and susceptibility to app updates. Recent advancements have utilized the view hierarchy to collect UI information and employed Large Language Models (LLM) to enhance task automation. However, view hierarchies have accessibility issues and face potential problems like missing object descriptions or misaligned structures. This paper introduces VisionTasker, a two-stage framework combining vision-based UI understanding and LLM task planning, for mobile task automation in a step-by-step manner. VisionTasker firstly converts a UI screenshot into natural language interpretations using a vision-based UI understanding approach, eliminating the need for view hierarchies. Secondly, it adopts a step-by-step task planning method, presenting one interface at a time to the LLM. The LLM then identifies relevant elements within the interface and determines the next action, enhancing accuracy and practicality. Extensive experiments show that VisionTasker outperforms previous methods, providing effective UI representations across four datasets. Additionally, in automating 147 real-world tasks on an Android smartphone, VisionTasker demonstrates advantages over humans in tasks where humans show unfamiliarity and shows significant improvements when integrated with the PBD mechanism. VisionTasker is open-source and available at https://github.com/AkimotoAyako/VisionTasker.




## Programming UI
### NotePlayer: Engaging Jupyter Notebooks for Dynamic Presentation of Analytical Processes
Authors: Yang Ouyang, Leixian Shen, Yun Wang, Quan Li

[Link](https://programs.sigchi.org/uist/2024/program/content/170819)

Abstract: Diverse presentation formats play a pivotal role in effectively conveying code and analytical processes during data analysis. One increasingly popular format is tutorial videos, particularly those based on Jupyter notebooks, which offer an intuitive interpretation of code and vivid explanations of analytical procedures. However, creating such videos requires a diverse skill set and significant manual effort, posing a barrier for many analysts. To bridge this gap, we introduce an innovative tool called NotePlayer, which connects notebook cells to video segments and incorporates a computational engine with language models to streamline video creation and editing. Our aim is to make the process more accessible and efficient for analysts. To inform the design of NotePlayer, we conducted a formative study and performed content analysis on a corpus of 38 Jupyter tutorial videos. This helped us identify key patterns and challenges encountered in existing tutorial videos, guiding the development of NotePlayer. Through a combination of a usage scenario and a user study, we validated the effectiveness of NotePlayer. The results show that the tool streamlines the video creation and facilitates the communication process for data analysts.



### Tyche: Making Sense of Property-Based Testing Effectiveness
Authors: Harrison Goldstein, Jeffrey Tao, Zac Hatfield-Dodds, Benjamin Pierce, Andrew Head

[Link](https://programs.sigchi.org/uist/2024/program/content/170922)

Abstract: Software developers increasingly rely on automated methods to assess the
correctness of their code. One such method is property-based testing
(PBT), wherein a test harness generates hundreds or thousands of inputs
and checks the outputs of the program on those inputs using parametric
properties. Though powerful, PBT induces a sizable gulf of evaluation:
developers need to put in nontrivial effort to understand how well the
different test inputs exercise the software under test. To bridge this
gulf, we propose Tyche, a user interface that supports sensemaking
around the effectiveness of property-based tests. Guided by a formative
design exploration, our design of Tyche supports developers with
interactive, configurable views of test behavior with tight integrations
into modern developer testing workflow. These views help developers
explore global testing behavior and individual test inputs alike. To
accelerate the development of powerful, interactive PBT tools, we define
a standard for PBT test reporting and integrate it with a widely used
PBT library. A self-guided online usability study revealed that Tyche's
visualizations help developers to more accurately assess software
testing effectiveness.




### CoLadder: Manipulating Code Generation via Multi-Level Blocks
Authors: Ryan Yen, Jiawen Zhu, Sangho Suh, Haijun Xia, Jian Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/171012)

Abstract: This paper adopted an iterative design process to gain insights into programmers' strategies when using LLMs for programming. We proposed CoLadder, a novel system that supports programmers by facilitating hierarchical task decomposition, direct code segment manipulation, and result evaluation during prompt authoring. A user study with 12 experienced programmers showed that CoLadder is effective in helping programmers externalize their problem-solving intentions flexibly, improving their ability to evaluate and modify code across various abstraction levels, from their task's goal to final code implementation.



### SQLucid: Grounding Natural Language Database Queries with Interactive Explanations
Authors: Yuan Tian, Jonathan Kummerfeld, Toby Li, Tianyi Zhang

[Link](https://programs.sigchi.org/uist/2024/program/content/170951)

Abstract: Though recent advances in machine learning have led to significant improvements in natural language interfaces for databases, the accuracy and reliability of these systems remain limited, especially in high-stakes domains. This paper introduces SQLucid, a novel user interface that bridges the gap between non-expert users and complex database querying processes. SQLucid addresses existing limitations by integrating visual correspondence, intermediate query results, and editable step-by-step SQL explanations in natural language to facilitate user understanding and engagement. This unique blend of features empowers users to understand and refine SQL queries easily and precisely. Two user studies and one quantitative experiment were conducted to validate SQLucid’s effectiveness, showing significant improvement in task completion accuracy and user confidence compared to existing interfaces. Our code is available at https://github.com/magic-YuanTian/SQLucid.




## Next Gen Input
### PointerVol: A Laser Pointer for Swept Volumetric Displays
Authors: Unai Javier Fernández, Iosune Sarasate Azcona, Iñigo Ezcurdia, Manuel Lopez-Amo, Ivan Fernández, Asier Marzo

[Link](https://programs.sigchi.org/uist/2024/program/content/170724)

Abstract: A laser pointer is a commonly used device that does not require communication with the display system or modifications on the applications, the presenter can just take a pointer and start using it. When a laser pointer is used on a volumetric display, a line rather than a point appears, making it not suitable for pointing at 3D locations. PointerVol is a modified laser pointer that allows users to point to 3D positions inside a swept volumetric display. We propose two PointerVol implementations based on timing and distance measurements, we evaluate the pointing performance using them. Finally, we present other features such as multi-user pointing, line patterns and a multi-finger wearable. PointerVol is a simple device that can help to popularize volumetric displays, or at least to make them more usable for presentations with true-3D content.



### RFTIRTouch: Touch Sensing Device for Dual-sided Transparent Plane Based on Repropagated Frustrated Total Internal Reflection
Authors: Ratchanon Wattanaparinton, Kotaro Kitada, Kentaro Takemura

[Link](https://programs.sigchi.org/uist/2024/program/content/170876)

Abstract: Frustrated total internal reflection (FTIR) imaging is widely applied in various touch-sensing systems. However, vision-based touch sensing has structural constraints, and the system size tends to increase. Although a sensing system with reduced thickness has been developed recently using repropagated FTIR (RFTIR), it lacks the property of instant installation anywhere because observation from the side of a transparent medium is required. Therefore, this study proposes an "RFTIRTouch" sensing device to capture RFTIR images from the contact surface. RFTIRTouch detects the touch position on a dual-sided plane using a physics-based estimation and can be retrofitted to existing transparent media with simple calibration. Our evaluation experiments confirm that the touch position can be estimated within an error of approximately 2.1 mm under optimal conditions. Furthermore, several application examples are implemented to demonstrate the advantages of RFTIRTouch, such as its ability to measure dual sides with a single sensor and waterproof the contact surface.



### IRIS: Wireless Ring for Vision-based Smart Home Interaction
Authors: Maruchi Kim, Antonio Glenn, Bandhav Veluri, Yunseo Lee, Eyoel Gebre, Aditya Bagaria, Shwetak Patel, Shyamnath Gollakota

[Link](https://programs.sigchi.org/uist/2024/program/content/171018)

Abstract: Integrating cameras into wireless smart rings has been challenging due to size and power constraints. We introduce IRIS, the first wireless vision-enabled smart ring system for smart home interactions. Equipped with a camera, Bluetooth radio, inertial measurement unit (IMU), and an onboard battery, IRIS meets the small size, weight, and power (SWaP) requirements for ring devices. IRIS is context-aware, adapting its gesture set to the detected device, and can last for 16-24 hours on a single charge. IRIS leverages the scene semantics to achieve instance-level device recognition. In a study involving 23 participants, IRIS consistently outpaced voice commands, with a higher proportion of participants expressing a preference for IRIS over voice commands regarding toggling a device's state, granular control, and social acceptability.  Our work pushes the  boundary of what is possible with ring form-factor devices, addressing system challenges and opening up novel interaction capabilities.



### Silent Impact: Tracking Tennis Shots from the Passive Arm
Authors: Junyong Park, Saelyne Yang, Sungho Jo

[Link](https://programs.sigchi.org/uist/2024/program/content/170795)

Abstract: Wearable technology has transformed sports analytics, offering new dimensions in enhancing player experience. Yet, many solutions involve cumbersome setups that inhibit natural motion. In tennis, existing products require sensors on the racket or dominant arm, causing distractions and discomfort. We propose Silent Impact, a novel and user-friendly system that analyzes tennis shots using a sensor placed on the passive arm. Collecting Inertial Measurement Unit sensor data from 20 recreational tennis players, we developed neural networks that exclusively utilize passive arm data to detect and classify six shots, achieving a classification accuracy of 88.2% and a detection F1 score of 86.0%, comparable to the dominant arm. These models were then incorporated into an end-to-end prototype, which records passive arm motion through a smartwatch and displays a summary of shots on a mobile app. User study (N=10) showed that participants felt less burdened physically and mentally using Silent Impact on the passive arm. Overall, our research establishes the passive arm as an effective, comfortable alternative for tennis shot analysis, advancing user-friendly sports analytics.




## LLM: New applications
### VoicePilot: Harnessing LLMs as Speech Interfaces for Assistive Robotics
Authors: Akhil Padmanabha, Jessie Yuan, Janavi Gupta, Zulekha Karachiwalla, Carmel Majidi, Henny Admoni, Zackory Erickson

[Link](https://programs.sigchi.org/uist/2024/program/content/170789)

Abstract: Physically assistive robots present an opportunity to significantly increase the well-being and independence of individuals with motor impairments or other forms of disability who are unable to complete activities of daily living. Speech interfaces, especially ones that utilize Large Language Models (LLMs), can enable individuals to effectively and naturally communicate high-level commands and nuanced preferences to robots. Frameworks for integrating LLMs as interfaces to robots for high level task planning and code generation have been proposed, but fail to incorporate human-centric considerations which are essential while developing assistive interfaces. In this work, we present a framework for incorporating LLMs as speech interfaces for physically assistive robots, constructed iteratively with 3 stages of testing involving a feeding robot, culminating in an evaluation with 11 older adults at an independent living facility. We use both quantitative and qualitative data from the final study to validate our framework and additionally provide design guidelines for using LLMs as speech interfaces for assistive robots. Videos, code, and supporting files are located on our project website\footnote{\url{https://sites.google.com/andrew.cmu.edu/voicepilot/}}



### ComPeer: A Generative Conversational Agent for Proactive Peer Support
Authors: Tianjian Liu, Hongzheng Zhao, Yuheng Liu, Xingbo Wang, Zhenhui Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170845)

Abstract: Conversational Agents (CAs) acting as peer supporters have been widely studied and demonstrated beneficial for people's mental health. However, previous peer support CAs either are user-initiated or follow predefined rules to initiate the conversations, which may discourage users to engage and build relationships with the CAs for long-term benefits. In this paper, we develop ComPeer, a generative CA that can proactively offer adaptive peer support to users. ComPeer leverages large language models to detect and reflect significant events in the dialogue, enabling it to strategically plan the timing and content of proactive care. In addition, ComPeer incorporates peer support strategies, conversation history, and its persona into the generative messages. Our one-week between-subjects study (N=24) demonstrates ComPeer's strength in providing peer support over time and boosting users' engagement compared to a baseline user-initiated CA. We report users' interaction patterns with ComPeer and discuss implications for designing proactive generative agents to promote people's well-being.



### SHAPE-IT: Exploring Text-to-Shape-Display for Generative Shape-Changing Behaviors with LLMs
Authors: Wanli Qian, Chenfeng Gao, Anup Sathya, Ryo Suzuki, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170820)

Abstract: This paper introduces text-to-shape-display, a novel approach to generating dynamic shape changes in pin-based shape displays through natural language commands. By leveraging large language models (LLMs) and AI-chaining, our approach allows users to author shape-changing behaviors on demand through text prompts without programming. We describe the foundational aspects necessary for such a system, including the identification of key generative elements (primitive, animation, and interaction) and design requirements to enhance user interaction, based on formative exploration and iterative design processes. Based on these insights, we develop SHAPE-IT, an LLM-based authoring tool for a 24 x 24 shape display, which translates the user's textual command into executable code and allows for quick exploration through a web-based control interface. We evaluate the effectiveness of SHAPE-IT in two ways: 1) performance evaluation and 2) user evaluation (N= 10). The study conclusions highlight the ability to facilitate rapid ideation of a wide range of shape-changing behaviors with AI. However, the findings also expose accuracy-related challenges and limitations, prompting further exploration into refining the framework for leveraging AI to better suit the unique requirements of shape-changing systems.



### WaitGPT: Monitoring and Steering Conversational LLM Agent in Data Analysis with On-the-Fly Code Visualization
Authors: Liwenhan Xie, Chengbo Zheng, Haijun Xia, Huamin Qu, Chen Zhu-Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/170828)

Abstract: Large language models (LLMs) support data analysis through conversational user interfaces, as exemplified in OpenAI's ChatGPT (formally known as Advanced Data Analysis or Code Interpreter). Essentially, LLMs produce code for accomplishing diverse analysis tasks. However, presenting raw code can obscure the logic and hinder user verification. To empower users with enhanced comprehension and augmented control over analysis conducted by LLMs, we propose a novel approach to transform LLM-generated code into an interactive visual representation. In the approach, users are provided with a clear, step-by-step visualization of the LLM-generated code in real time, allowing them to understand, verify, and modify individual data operations in the analysis. Our design decisions are informed by a formative study (N=8) probing into user practice and challenges. We further developed a prototype named WaitGPT and conducted a user study (N=12) to evaluate its usability and effectiveness. The findings from the user study reveal that WaitGPT facilitates monitoring and steering of data analysis performed by LLMs, enabling participants to enhance error detection and increase their overall confidence in the results.




## Break Q&A: Haptics
### LoopBot: Representing Continuous Haptics of Grounded Objects in Room-scale VR
Authors: Tetsushi Ikeda, Kazuyuki Fujita, Kumpei Ogawa, Kazuki Takashima, Yoshifumi Kitamura

[Link](https://programs.sigchi.org/uist/2024/program/content/171016)

Abstract: In room-scale virtual reality, providing continuous haptic feedback from touching grounded objects, such as walls and handrails, has been challenging due to the user's walking range and the required force. In this study, we propose LoopBot, a novel technique to provide continuous haptic feedback from grounded objects using only a single user-following robot. Specifically, LoopBot is equipped with a loop-shaped haptic prop attached to an omnidirectional robot that scrolls to cancel out the robot's displacement, giving the user the haptic sensation that the prop is actually fixed in place, or ``grounded.'' We first introduce the interaction design space of LoopBot and, as one of its promising interaction scenarios, implement a prototype for the experience of walking while grasping handrails. A performance evaluation shows that scrolling the prop cancels $77.5\%$ of the robot's running speed on average. A preliminary user test ($N=10$) also shows that the subjective realism of the experience and the sense of the virtual handrails being grounded were significantly higher than when the prop was not scrolled. Based on these findings, we discuss possible further development of LoopBot.



### JetUnit: Rendering Diverse Force Feedback in Virtual Reality Using Water Jets
Authors: Zining Zhang, Jiasheng Li, Zeyu Yan, Jun Nishida, Huaishu Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170767)

Abstract: We propose JetUnit, a water-based VR haptic system designed to produce force feedback with a wide spectrum of intensities and frequencies through water jets. The key challenge in designing this system lies in optimizing parameters to enable the haptic device to generate force feedback that closely replicates the most intense force produced by direct water jets while ensuring the user remains dry. In this paper, we present the key design parameters of the JetUnit wearable device determined through a set of quantitative experiments and a perception study. We further conducted a user study to assess the impact of integrating our haptic solutions into virtual reality experiences. The results revealed that, by adhering to the design principles of JetUnit, the water-based haptic system is capable of delivering diverse force feedback sensations, significantly enhancing the immersive experience in virtual reality.



### Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions
Authors: Takeru Hashimoto, Yutaro Hirao

[Link](https://programs.sigchi.org/uist/2024/program/content/170833)

Abstract: We propose Selfrionette, a controller that uses fingertip force input to drive avatar movements in virtual reality (VR). 
This system enables users to interact with virtual objects and walk in VR using only fingertip force, overcoming physical and spatial constraints. Additionally, by fixing users' fingers, it provides users with counterforces equivalent to the applied force, allowing for diverse and wide dynamic range haptic feedback by adjusting the relationship between force input and virtual movement.
To evaluate the effectiveness of the proposed method, this paper focuses on hand interaction as a first step.
In User Study 1, we measured usability and embodiment during reaching tasks under Selfrionette, body tracking, and finger tracking conditions.
In User Study 2, we investigated whether users could perceive haptic properties such as weight, friction, and compliance under the same conditions as User Study 1.
Selfrionette was found to be comparable to body tracking in realism of haptic interaction, enabling embodied avatar experiences even in limited spatial conditions.



### SpinShot: Optimizing Both Physical and Perceived Force Feedback of Flywheel-Based, Directional Impact Handheld Devices
Authors: Chia-An Fan, En-Huei Wu, Chia-Yu Cheng, Yu-Cheng Chang, Alvaro Lopez, Yu Chen, Chia-Chen Chi, Yi-Sheng Chan, Ching-Yi Tsai, Mike Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170972)

Abstract: Real-world impact, such as hitting a tennis ball and a baseball, generates instantaneous, directional impact forces. However, current ungrounded force feedback technologies, such as air jets and propellers, can only generate directional impulses that are 10x-10,000x weaker. We present SpinShot, a flywheel-based device with a solenoid-actuated stopper capable of generating directional impulse of 22Nm in 1ms, which is more than 10x stronger than prior ungrounded directional technologies. Furthermore, we present a novel force design that reverses the flywheel immediately after the initial impact, to significantly increase the perceived magnitude. We conducted a series of two formative, perceptual studies (n=16, 18), followed by a summative user experience study (n=16) that compared SpinShot vs. moving mass (solenoid) and vs. air jets in a VR baseball hitting game. Results showed that SpinShot significantly improved realism, immersion, magnitude (p < .01) compared to both baselines, but significantly reduced comfort vs. air jets primarily due to the 2.9x device weight. Overall, SpinShot was preferred by 63-75% of the participants.




## Break Q&A: Body as the interface
### MouthIO: Fabricating Customizable Oral User Interfaces with Integrated Sensing and Actuation
Authors: Yijing Jiang, Julia Kleinau, Till Max Eckroth, Eve Hoggan, Stefanie Mueller, Michael Wessely

[Link](https://programs.sigchi.org/uist/2024/program/content/170798)

Abstract: This paper introduces MouthIO, the first customizable intraoral user interface that can be equipped with various sensors and output components. MouthIO consists of an SLA-printed brace that houses a flexible PCB within a bite-proof enclosure positioned between the molar teeth and inner cheeks. Our MouthIO design and fabrication technique enables makers to customize the oral user interfaces in both form and function at low cost. All parts in contact with the oral cavity are made of bio-compatible materials to ensure safety, while the design takes into account both comfort and portability. We demonstrate MouthIO through three application examples ranging from beverage consumption monitoring, health monitoring, to assistive technology. Results from our full-day user study indicate high wearability and social acceptance levels, while our technical evaluation demonstrates the device's ability to withstand adult bite forces.



### Can a Smartwatch Move Your Fingers? Compact and Practical Electrical Muscle Stimulation in a Smartwatch
HONORABLE_MENTION

Authors: Akifumi Takahashi, Yudai Tanaka, Archit Tamhane, Alan Shen, Shan-Yuan Teng, Pedro Lopes

[Link](https://programs.sigchi.org/uist/2024/program/content/170990)

Abstract: Smartwatches gained popularity in the mainstream, making them into today’s de-facto wearables. Despite advancements in sensing, haptics on smartwatches is still restricted to tactile feedback (e.g., vibration). Most smartwatch-sized actuators cannot render strong force-feedback. Simultaneously, electrical muscle stimulation (EMS) promises compact force-feedback but, to actuate fingers requires users to wear many electrodes on their forearms. While forearm electrodes provide good accuracy, they detract EMS from being a practical force-feedback interface. To address this, we propose moving the electrodes to the wrist—conveniently packing them in the backside of a smartwatch. In our first study, we found that by cross-sectionally stimulating the wrist in 1,728 trials, we can actuate thumb extension, index extension & flexion, middle flexion, pinky flexion, and wrist flexion. Following, we engineered a compact EMS that integrates directly into a smartwatch’s wristband (with a custom stimulator, electrodes, demultiplexers, and communication). In our second study, we found that participants could calibrate our device by themselves ~50% faster than with conventional EMS. Furthermore, all participants preferred the experience of this device, especially for its social acceptability & practicality. We believe that our approach opens new applications for smartwatch-based interactions, such as haptic assistance during everyday tasks.



### Power-over-Skin: Full-Body Wearables Powered By Intra-Body RF Energy
Authors: Andy Kong, Daehwa Kim, Chris Harrison

[Link](https://programs.sigchi.org/uist/2024/program/content/170775)

Abstract: Powerful computing devices are now small enough to be easily worn on the body. However, batteries pose a major design and user experience obstacle, adding weight and volume, and generally requiring periodic device removal and recharging. In response, we developed Power-over-Skin, an approach using the human body itself to deliver power to many distributed, battery-free, worn devices. We demonstrate power delivery from on-body distances as far as from head-to-toe, with sufficient energy to power microcontrollers capable of sensing and wireless communication. We share results from a study campaign that informed our implementation, as well as experiments that validate our final system. We conclude with several demonstration devices, ranging from input controllers to longitudinal bio-sensors, which highlight the efficacy and potential of our approach.



### HandPad: Make Your Hand an On-the-go Writing Pad via Human Capacitance
Authors: Yu Lu, Dian Ding, Hao Pan, Yijie Li, Juntao Zhou, Yongjian Fu, Yongzhao Zhang, Yi-Chao Chen, Guangtao Xue

[Link](https://programs.sigchi.org/uist/2024/program/content/170761)

Abstract: The convenient text input system is a pain point for devices such as AR glasses, and it is difficult for existing solutions to balance portability and efficiency. This paper introduces HandPad, the system that turns the hand into an on-the-go touchscreen, which realizes interaction on the hand via human capacitance. HandPad achieves keystroke and handwriting inputs for letters, numbers, and Chinese characters, reducing the dependency on capacitive or pressure sensor arrays. Specifically, the system verifies the feasibility of touch point localization on the hand using the human capacitance model and proposes a handwriting recognition system based on Bi-LSTM and ResNet. The transfer learning-based system only needs a small amount of training data to build a handwriting recognition model for the target user. Experiments in real environments verify the feasibility of HandPad for keystroke (accuracy of 100%) and handwriting recognition for letters (accuracy of 99.1%), numbers (accuracy of 97.6%) and Chinese characters (accuracy of 97.9%).




## Break Q&A: Vision-based UIs
### Vision-Based Hand Gesture Customization from a Single Demonstration
Authors: Soroush Shahi, Vimal Mollyn, Cori Tymoszek Park, Runchang Kang, Asaf Liberman, Oron Levy, Jun Gong, Abdelkareem Bedri, Gierad Laput

[Link](https://programs.sigchi.org/uist/2024/program/content/170938)

Abstract: Hand gesture recognition is becoming a more prevalent mode of human-computer interaction, especially as cameras proliferate across everyday devices. Despite continued progress in this field, gesture customization is often underexplored. Customization is crucial since it enables users to define and demonstrate gestures that are more natural, memorable, and accessible. However, customization requires efficient usage of user-provided data. We introduce a method that enables users to easily design bespoke gestures with a monocular camera from one demonstration. We employ transformers and meta-learning techniques to address few-shot learning challenges. Unlike prior work, our method supports any combination of one-handed, two-handed, static, and dynamic gestures, including different viewpoints, and the ability to handle irrelevant hand movements. We implement three real-world applications using our customization method, conduct a user study, and achieve up to 94\% average recognition accuracy from one demonstration. Our work provides a viable path for vision-based gesture customization, laying the foundation for future advancements in this domain. 



### VirtualNexus: Enhancing 360-Degree Video AR/VR Collaboration with Environment Cutouts and Virtual Replicas
Authors: Xincheng Huang, Michael Yin, Ziyi Xia, Robert Xiao

[Link](https://programs.sigchi.org/uist/2024/program/content/170877)

Abstract: Asymmetric AR/VR collaboration systems bring a remote VR user to a local AR user’s physical environment, allowing them to communicate and work within a shared virtual/physical space. Such systems often display the remote environment through 3D reconstructions or 360° videos. While 360° cameras stream an environment in higher quality, they lack spatial information, making them less interactable. We present VirtualNexus, an AR/VR collaboration system that enhances 360° video AR/VR collaboration with environment cutouts and virtual replicas. VR users can define cutouts of the remote environment to interact with as a world-in-miniature, and their interactions are synchronized to the local AR perspective. Furthermore, AR users can rapidly scan and share 3D virtual replicas of physical objects using neural rendering. We demonstrated our system’s utility through 3 example applications and evaluated our system in a dyadic usability test. VirtualNexus extends the interaction space of 360° telepresence systems, offering improved physical presence, versatility, and clarity in interactions. 



### Personal Time-Lapse
Authors: Nhan Tran, Ethan Yang, Angelique Taylor, Abe Davis

[Link](https://programs.sigchi.org/uist/2024/program/content/170932)

Abstract: Our bodies are constantly in motion—from the bending of arms and legs to the less conscious movement of breathing, our precise shape and location change constantly. This can make subtler developments (e.g., the growth of hair, or the healing of a wound) difficult to observe. Our work focuses on helping users record and visualize this type of subtle, longer-term change. We present a mobile tool that combines custom 3D tracking with interactive visual feedback and computational imaging to capture personal time-lapse, which approximates longer-term video of the subject (typically, part of the capturing user’s body) under a fixed viewpoint, body pose, and lighting condition. These personal time-lapses offer a powerful and detailed way to track visual changes of the subject over time. We begin with a formative study that examines what makes personal time-lapse so difficult to capture. Building on our findings, we motivate the design of our capture tool, evaluate this design with users, and demonstrate its effectiveness in a variety of challenging examples.



### Chromaticity Gradient Mapping for Interactive Control of Color Contrast in Images and Video
Authors: Ruyu Yan, Jiatian Sun, Abe Davis

[Link](https://programs.sigchi.org/uist/2024/program/content/170867)

Abstract: We present a novel perceptually-motivated interactive tool for using color contrast to enhance details represented in the lightness channel of images and video. Our method lets users adjust the perceived contrast of different details by manipulating local chromaticity while preserving the original lightness of individual pixels. Inspired by the use of similar chromaticity mappings in painting, our tool effectively offers contrast along a user-selected gradient of chromaticities as additional bandwidth for representing and enhancing different details in an image. We provide an interface for our tool that closely resembles the familiar design of tonal contrast curve controls that are available in most professional image editing software. We show that our tool is effective for enhancing the perceived contrast of details without altering lightness in an image and present many examples of effects that can be achieved with our method on both images and video.




## Break Q&A: Next Gen Input
### PointerVol: A Laser Pointer for Swept Volumetric Displays
Authors: Unai Javier Fernández, Iosune Sarasate Azcona, Iñigo Ezcurdia, Manuel Lopez-Amo, Ivan Fernández, Asier Marzo

[Link](https://programs.sigchi.org/uist/2024/program/content/170724)

Abstract: A laser pointer is a commonly used device that does not require communication with the display system or modifications on the applications, the presenter can just take a pointer and start using it. When a laser pointer is used on a volumetric display, a line rather than a point appears, making it not suitable for pointing at 3D locations. PointerVol is a modified laser pointer that allows users to point to 3D positions inside a swept volumetric display. We propose two PointerVol implementations based on timing and distance measurements, we evaluate the pointing performance using them. Finally, we present other features such as multi-user pointing, line patterns and a multi-finger wearable. PointerVol is a simple device that can help to popularize volumetric displays, or at least to make them more usable for presentations with true-3D content.



### RFTIRTouch: Touch Sensing Device for Dual-sided Transparent Plane Based on Repropagated Frustrated Total Internal Reflection
Authors: Ratchanon Wattanaparinton, Kotaro Kitada, Kentaro Takemura

[Link](https://programs.sigchi.org/uist/2024/program/content/170876)

Abstract: Frustrated total internal reflection (FTIR) imaging is widely applied in various touch-sensing systems. However, vision-based touch sensing has structural constraints, and the system size tends to increase. Although a sensing system with reduced thickness has been developed recently using repropagated FTIR (RFTIR), it lacks the property of instant installation anywhere because observation from the side of a transparent medium is required. Therefore, this study proposes an "RFTIRTouch" sensing device to capture RFTIR images from the contact surface. RFTIRTouch detects the touch position on a dual-sided plane using a physics-based estimation and can be retrofitted to existing transparent media with simple calibration. Our evaluation experiments confirm that the touch position can be estimated within an error of approximately 2.1 mm under optimal conditions. Furthermore, several application examples are implemented to demonstrate the advantages of RFTIRTouch, such as its ability to measure dual sides with a single sensor and waterproof the contact surface.



### IRIS: Wireless Ring for Vision-based Smart Home Interaction
Authors: Maruchi Kim, Antonio Glenn, Bandhav Veluri, Yunseo Lee, Eyoel Gebre, Aditya Bagaria, Shwetak Patel, Shyamnath Gollakota

[Link](https://programs.sigchi.org/uist/2024/program/content/171018)

Abstract: Integrating cameras into wireless smart rings has been challenging due to size and power constraints. We introduce IRIS, the first wireless vision-enabled smart ring system for smart home interactions. Equipped with a camera, Bluetooth radio, inertial measurement unit (IMU), and an onboard battery, IRIS meets the small size, weight, and power (SWaP) requirements for ring devices. IRIS is context-aware, adapting its gesture set to the detected device, and can last for 16-24 hours on a single charge. IRIS leverages the scene semantics to achieve instance-level device recognition. In a study involving 23 participants, IRIS consistently outpaced voice commands, with a higher proportion of participants expressing a preference for IRIS over voice commands regarding toggling a device's state, granular control, and social acceptability.  Our work pushes the  boundary of what is possible with ring form-factor devices, addressing system challenges and opening up novel interaction capabilities.



### Silent Impact: Tracking Tennis Shots from the Passive Arm
Authors: Junyong Park, Saelyne Yang, Sungho Jo

[Link](https://programs.sigchi.org/uist/2024/program/content/170795)

Abstract: Wearable technology has transformed sports analytics, offering new dimensions in enhancing player experience. Yet, many solutions involve cumbersome setups that inhibit natural motion. In tennis, existing products require sensors on the racket or dominant arm, causing distractions and discomfort. We propose Silent Impact, a novel and user-friendly system that analyzes tennis shots using a sensor placed on the passive arm. Collecting Inertial Measurement Unit sensor data from 20 recreational tennis players, we developed neural networks that exclusively utilize passive arm data to detect and classify six shots, achieving a classification accuracy of 88.2% and a detection F1 score of 86.0%, comparable to the dominant arm. These models were then incorporated into an end-to-end prototype, which records passive arm motion through a smartwatch and displays a summary of shots on a mobile app. User study (N=10) showed that participants felt less burdened physically and mentally using Silent Impact on the passive arm. Overall, our research establishes the passive arm as an effective, comfortable alternative for tennis shot analysis, advancing user-friendly sports analytics.




## Break Q&A: Future of Typing
### OptiBasePen: Mobile Base+Pen Input on Passive Surfaces by Sensing Relative Base Motion Plus Close-Range Pen Position
Authors: Andreas Fender, Mohamed Kari

[Link](https://programs.sigchi.org/uist/2024/program/content/170879)

Abstract: Digital pen input devices based on absolute pen position sensing, such as Wacom Pens, support high-fidelity pen input. However, they require specialized sensing surfaces like drawing tablets, which can have a large desk footprint, constrain the possible input area, and limit mobility. In contrast, digital pens with integrated relative sensing enable mobile use on passive surfaces, but suffer from motion artifacts or require surface contact at all times, deviating from natural pen affordances. We present OptiBasePen, a device for mobile pen input on ordinary surfaces. Our prototype consists of two parts: the "base" on which the hand rests and the pen for fine-grained input. The base features a high-precision mouse sensor to sense its own relative motion, and two infrared image sensors to track the absolute pen tip position within the base's frame of reference. This enables pen input on ordinary surfaces without external cameras while also avoiding drift from pen micro-movements. In this work, we present our prototype as well as the general base+pen concept, which combines relative and absolute sensing.



### Palmrest+: Expanding Laptop Input Space with Shear Force on Palm-Resting Area
Authors: Jisu Yim, Seoyeon Bae, Taejun Kim, Sunbum Kim, Geehyuk Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170781)

Abstract: The palmrest area of laptops has the potential as an additional input space, considering its consistent palm contact during keyboard interaction. We propose Palmrest+, leveraging shear force exerted on the palmrest area. We suggest two input techniques: Palmrest Shortcut, for instant shortcut execution, and Palmrest Joystick, for continuous value input. These allow seamless and subtle input amidst keyboard typing. Evaluation of Palmrest Shortcut against conventional keyboard shortcuts revealed faster performance for applying shear force in unimanual and bimanual-manner with a significant reduction in gaze shifting. Additionally, the assessment of Palmrest Joystick against the laptop touchpad demonstrated comparable performance in selecting one- and two- dimensional targets with low-precision pointing, i.e., for short distances and large target sizes. The maximal hand displacement significantly decreased for both Palmrest Shortcut and Palmrest Joystick compared to conventional methods. These findings verify the feasibility and effectiveness of leveraging the palmrest area as an additional input space on laptops, offering promising enhanced typing-related user interaction experiences.



### TouchInsight: Uncertainty-aware Rapid Touch and Text Input for Mixed Reality from Egocentric Vision
Authors: Paul Streli, Mark Richardson, Fadi Botros, Shugao Ma, Robert Wang, Christian Holz

[Link](https://programs.sigchi.org/uist/2024/program/content/170817)

Abstract: While passive surfaces offer numerous benefits for interaction in mixed reality, reliably detecting touch input solely from head-mounted cameras has been a long-standing challenge. Camera specifics, hand self-occlusion, and rapid movements of both head and fingers introduce considerable uncertainty about the exact location of touch events. Existing methods have thus not been capable of achieving the performance needed for robust interaction.
In this paper, we present a real-time pipeline that detects touch input from all ten fingers on any physical surface, purely based on egocentric hand tracking. Our method TouchInsight comprises a neural network to predict the moment of a touch event, the finger making contact, and the touch location. TouchInsight represents locations through a bivariate Gaussian distribution to account for uncertainties due to sensing inaccuracies, which we resolve through contextual priors to accurately infer intended user input.
We first evaluated our method offline and found that it locates input events with a mean error of 6.3 mm, and accurately detects touch events (F1=0.99) and identifies the finger used (F1=0.96). In an online evaluation, we then demonstrate the effectiveness of our approach for a core application of dexterous touch input: two-handed text entry. In our study, participants typed 37.0 words per minute with an uncorrected error rate of 2.9% on average.



### Can Capacitive Touch Images Enhance Mobile Keyboard Decoding?
Authors: Piyawat Lertvittayakumjorn, Shanqing Cai, Billy Dou, Cedric Ho, Shumin Zhai

[Link](https://programs.sigchi.org/uist/2024/program/content/170719)

Abstract: Capacitive touch sensors capture the two-dimensional spatial profile (referred to as a touch heatmap) of a finger's contact with a mobile touchscreen. However, the research and design of touchscreen mobile keyboards -- one of the most speed and accuracy demanding touch interfaces -- has focused on the location of the touch centroid derived from the touch image heatmap as the input, discarding the rest of the raw spatial signals. In this paper, we investigate whether touch heatmaps can be leveraged to further improve the tap decoding accuracy for mobile touchscreen keyboards. Specifically, we developed and evaluated machine-learning models that interpret user taps by using the centroids and/or the heatmaps as their input and studied the contribution of the heatmaps to model performance. The results show that adding the heatmap into the input feature set led to 21.4% relative reduction of character error rates on average, compared to using the centroid alone. Furthermore, we conducted a live user study with the centroid-based and heatmap-based decoders built into Pixel 6 Pro devices and observed lower error rate, faster typing speed, and higher self-reported satisfaction score based on the heatmap-based decoder than the centroid-based decoder. These findings underline the promise of utilizing touch heatmaps for improving typing experience in mobile keyboards.




## Break Q&A: Storytime
### Story-Driven: Exploring the Impact of Providing Real-time Context Information on Automated Storytelling
Authors: Jan Henry Belz, Lina Weilke, Anton Winter, Philipp Hallgarten, Enrico Rukzio, Tobias Grosse-Puppendahl

[Link](https://programs.sigchi.org/uist/2024/program/content/170763)

Abstract: Stories have long captivated the human imagination with narratives that enrich our lives. Traditional storytelling methods are often static and not designed to adapt to the listener’s environment, which is full of dynamic changes. For instance, people often listen to stories in the form of podcasts or audiobooks while traveling in a car. Yet, conventional in-car storytelling systems do not embrace the adaptive potential of this space. The advent of generative AI is the key to creating content that is not just personalized but also responsive to the changing parameters of the environment. We introduce a novel system for interactive, real-time story narration that leverages environment and user context in correspondence with estimated arrival times to adjust the generated story continuously. Through two comprehensive real-world studies with a total of 30 participants in a vehicle, we assess the user experience, level of immersion, and perception of the environment provided by the prototype. Participants' feedback shows a significant improvement over traditional storytelling and highlights the importance of context information for generative storytelling systems. 



### Lumina: A Software Tool for Fostering Creativity in Designing Chinese Shadow Puppets
Authors: Zhihao Yao, Yao Lu, Qirui Sun, Shiqing Lyu, Hanxuan Li, Xing-Dong Yang, Xuezhu Wang, Guanhong Liu, Haipeng Mi

[Link](https://programs.sigchi.org/uist/2024/program/content/170765)

Abstract: Shadow puppetry, a culturally rich storytelling art, faces challenges transitioning to the digital realm. Creators in the early design phase struggle with crafting intricate patterns, textures, and basic animations while adhering to stylistic conventions - hindering creativity, especially for novices. This paper presents Lumina, a tool to facilitate the early Chinese shadow puppet design stage. Lumina provides contour templates, animations, scene editing tools, and machine-generated traditional puppet patterns. These features liberate creators from tedious tasks, allowing focus on the creative process. Developed based on a formative study with puppet creators, the web-based Lumina enables wide dissemination. An evaluation with 18 participants demonstrated Lumina's effectiveness and ease of use, with participants successfully creating designs spanning traditional themes to contemporary and science-fiction concepts.



### PortalInk: 2.5D Visual Storytelling with SVG Parallax and Waypoint Transitions
Authors: Tongyu Zhou, Joshua Yang, Vivian Chan, Ji Won Chung, Jeff Huang

[Link](https://programs.sigchi.org/uist/2024/program/content/170783)

Abstract: Efforts to expand the authoring of visual stories beyond the 2D canvas have commonly mapped flat imagery to 3D scenes or objects. This translation requires spatial reasoning, as artists must think in two spaces. We propose PortalInk, a tool for artists to craft and export 2.5D graphical stories while remaining in 2D space by using SVG transitions. This is achieved via a parallax effect that generates a sense of depth that can be further explored using pan and zoom interactions. Any canvas position can be saved and linked to in a closed drawn stroke, or "portal," allowing the artist to create spatially discontinuous, or even infinitely looping visual trajectories. We provide three case studies and a gallery to demonstrate how artists can naturally incorporate these interactions to craft immersive comics, as well as re-purpose them to support use cases beyond drawing such as animation, slide-based presentations, web design, and digital journalism.



### DrawTalking: Building Interactive Worlds by Sketching and Speaking
Authors: Karl Rosenberg, Rubaiat Habib Kazi, Li-Yi Wei, Haijun Xia, Ken Perlin

[Link](https://programs.sigchi.org/uist/2024/program/content/170730)

Abstract: We introduce DrawTalking, an approach to building and controlling interactive worlds by sketching and speaking while telling stories. It emphasizes user control and flexibility, and gives programming-like capability without requiring code. An early open-ended study with our prototype shows that the mechanics resonate and are applicable to many creative-exploratory use cases, with the potential to inspire and inform research in future natural interfaces for creative exploration and authoring.



### Patchview: LLM-powered Worldbuilding with Generative Dust and Magnet Visualization
Authors: John Chung, Max Kreminski

[Link](https://programs.sigchi.org/uist/2024/program/content/170729)

Abstract: Large language models (LLMs) can help writers build story worlds by generating world elements, such as factions, characters, and locations. However, making sense of many generated elements can be overwhelming. Moreover, if the user wants to precisely control aspects of generated elements that are difficult to specify verbally, prompting alone may be insufficient. We introduce Patchview, a customizable LLM-powered system that visually aids worldbuilding by allowing users to interact with story concepts and elements through the physical metaphor of magnets and dust. Elements in Patchview are visually dragged closer to concepts with high relevance, facilitating sensemaking. The user can also steer the generation with verbally elusive concepts by indicating the desired position of the element between concepts. When the user disagrees with the LLM's visualization and generation, they can correct those by repositioning the element. These corrections can be used to align the LLM's future behaviors to the user's perception. With a user study, we show that Patchview supports the sensemaking of world elements and steering of element generation, facilitating exploration during the worldbuilding process. Patchview provides insights on how customizable visual representation can help sensemake, steer, and align generative AI model behaviors with the user's intentions.



### An Interactive System for Suporting Creative Exploration of Cinematic Composition Designs
Authors: Rui He, Huaxin Wei, Ying Cao

[Link](https://programs.sigchi.org/uist/2024/program/content/170806)

Abstract: Designing cinematic compositions, which involves moving cameras through a scene, is essential yet challenging in filmmaking. Machinima filmmaking provides real-time virtual environments for exploring different compositions flexibly and efficiently. However, producing high-quality cinematic compositions in such environments still requires significant cinematography skills and creativity. This paper presents Cinemassist, a tool designed to support and enhance this creative process by generating a variety of cinematic composition proposals at both keyframe and scene levels, which users can incorporate into their workflows and achieve more creative results. At the crux of our system is a deep generative model trained on real movie data, which can generate plausible, diverse camera poses conditioned on 3D animations and additional input semantics. Our model enables an interactive cinematic composition design workflow where users can co-design with the model by being inspired by model-generated suggestions while having control over the generation process. Our user study and expert rating find Cinemassist can facilitate the design process for users of different backgrounds and enhance the design quality especially for users with animation expertise, demonstrating its potential as an invaluable tool in the context of digital filmmaking.




## Break Q&A: Manipulating Text
### Beyond the Chat: Executable and Verifiable Text-Editing with LLMs
Authors: Philippe Laban, Jesse Vig, Marti Hearst, Caiming Xiong, Chien-Sheng Wu

[Link](https://programs.sigchi.org/uist/2024/program/content/170790)

Abstract: Conversational interfaces powered by Large Language Models (LLMs) have recently become a popular way to obtain feedback during document editing. However, standard chat-based conversational interfaces cannot explicitly surface the editing changes that they suggest. To give the author more control when editing with an LLM, we present InkSync, an editing interface that suggests executable edits directly within the document being edited. Because LLMs are known to introduce factual errors, Inksync also supports a 3-stage approach to mitigate this risk: Warn authors when a suggested edit introduces new information, help authors Verify the new information's accuracy through external search, and allow a third party to Audit with a-posteriori verification via a trace of all auto-generated content.
Two usability studies confirm the effectiveness of InkSync's components when compared to standard LLM-based chat interfaces, leading to more accurate and more efficient editing, and improved user experience.



### ScriptViz: A Visualization Tool to Aid Scriptwriting based on a Large Movie Database
Authors: Anyi Rao, Jean-Peïc Chou, Maneesh Agrawala

[Link](https://programs.sigchi.org/uist/2024/program/content/170838)

Abstract: Scriptwriters usually rely on their mental visualization to create a vivid story by using their imagination to see, feel, and experience the scenes they are writing. Besides mental visualization, they often refer to existing images or scenes in movies and analyze the visual elements to create a certain mood or atmosphere. In this paper, we develop a new tool, ScriptViz, to provide external visualization based on a large movie database for the screenwriting process. It retrieves reference visuals on the fly based on scripts’ text and dialogue from a large movie database. The tool provides two types of control on visual elements that enable writers to 1) see exactly what they want with fixed visual elements and 2) see variances in uncertain elements. User evaluation among 15 scriptwriters shows that ScriptViz is able to present scriptwriters with consistent yet diverse visual possibilities, aligning closely with their scripts and helping their creation.




### SkipWriter: LLM-Powered Abbreviated Writing on Tablets
Authors: Zheer Xu, Shanqing Cai, Mukund Varma T, Subhashini Venugopalan, Shumin Zhai

[Link](https://programs.sigchi.org/uist/2024/program/content/170930)

Abstract: Large Language Models (LLMs) may offer transformative opportunities for text input, especially for physically demanding modalities like handwriting. We studied a form of abbreviated handwriting by designing, developing, and evaluating a prototype, named SkipWriter, that converts handwritten strokes of a variable-length prefix-based abbreviation (e.g. "ho a y" as handwritten strokes) into the intended full phrase (e.g., "how are you" in the digital format) based on the preceding context. SkipWriter consists of an in-production handwriting recognizer and an LLM fine-tuned on this task. With flexible pen input, SkipWriter allows the user to add and revise prefix strokes when predictions do not match the user's intent. An user evaluation demonstrated a 60% reduction in motor movements with an average speed of 25.78 WPM. We also showed that this reduction is close to the ceiling of our model in an offline simulation.



### Bluefish: Composing Diagrams with Declarative Relations
Authors: Josh Pollock, Catherine Mei, Grace Huang, Elliot Evans, Daniel Jackson, Arvind Satyanarayan

[Link](https://programs.sigchi.org/uist/2024/program/content/170824)

Abstract: Diagrams are essential tools for problem-solving and communication as they externalize conceptual structures using spatial relationships. But when picking a diagramming framework, users are faced with a dilemma. They can either use a highly expressive but low-level toolkit, whose API does not match their domain-specific concepts, or select a high-level typology, which offers a recognizable vocabulary but supports a limited range of diagrams. To address this gap, we introduce Bluefish: a diagramming framework inspired by component-based user interface (UI) libraries. Bluefish lets users create diagrams using relations: declarative, composable, and extensible diagram fragments that relax the concept of a UI component. Unlike a component, a relation does not have sole ownership over its children nor does it need to fully specify their layout. To render diagrams, Bluefish extends a traditional tree-based scenegraph to a compound graph that captures both hierarchical and adjacent relationships between nodes. To evaluate our system, we construct a diverse example gallery covering many domains including mathematics, physics, computer science, and even cooking. We show that Bluefish's relations are effective declarative primitives for diagrams. Bluefish is open source, and we aim to shape it into both a usable tool and a research platform.




## Break Q&A: Hot Interfaces
### Fiery Hands: Designing Thermal Glove through Thermal and Tactile Integration for Virtual Object Manipulation
Authors: Haokun Wang, Yatharth Singhal, Hyunjae Gil, Jin Ryong Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170880)

Abstract: We present a novel approach to render thermal and tactile feedback to the palm and fingertips through thermal and tactile integration. Our approach minimizes the obstruction of the palm and inner side of the fingers and enables virtual object manipulation while providing localized and global thermal feedback. By leveraging thermal actuators positioned strategically on the outer palm and back of the fingers in interplay with tactile actuators, our approach exploits thermal referral and tactile masking phenomena. Through a series of user studies, we validate the perception of localized thermal sensations across the palm and fingers, showcasing the ability to generate diverse thermal patterns. Furthermore, we demonstrate the efficacy of our approach in VR applications,  replicating diverse thermal interactions with virtual objects. This work represents significant progress in thermal interactions within VR, offering enhanced sensory immersion at an optimal energy cost.



### DexteriSync: A Hand Thermal I/O Exoskeleton for Morphing Finger Dexterity Experience
Authors: Ximing Shen, Youichi Kamiyama, Kouta Minamizawa, Jun Nishida

[Link](https://programs.sigchi.org/uist/2024/program/content/170898)

Abstract: Skin temperature is an important physiological factor for human hand dexterity. Leveraging this feature, we engineered an exoskeleton, called DexteriSync, that can dynamically adjust the user's finger dexterity and induce different thermal perceptions by modulating finger skin temperature. This exoskeleton comprises flexible silicone-copper tube segments, 3D-printed finger sockets, a 3D-printed palm base, a pump system, and a water temperature control with a storage unit. By realising an embodied experience of compromised dexterity, DexteriSync can help product designers understand the lived experience of compromised hand dexterity, such as that of the elderly and/or neurodivergent users, when designing daily necessities for them. We validated DexteriSync via a technical evaluation and two user studies, demonstrating that it can change skin temperature, dexterity, and thermal perception. An exploratory session with design students and an autistic compromised dexterity individual, demonstrated the exoskeleton provided a more realistic experience compared to video education, and allowed them to gain higher confidence in their designs. The results advocated for the efficacy of experiencing embodied compromised finger dexterity, which can promote an understanding of the related physical challenges and lead to a more persuasive design for assistive tools.



### Flip-Pelt: Motor-Driven Peltier Elements for Rapid Thermal Stimulation and Congruent Pressure Feedback in Virtual Reality
Authors: Seongjun Kang, Gwangbin Kim, Seokhyun Hwang, Jeongju Park, Ahmed Elsharkawy, SeungJun Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170885)

Abstract: This study introduces "Flip-Pelt," a motor-driven peltier device designed to provide rapid thermal stimulation and congruent pressure feedback in virtual reality (VR) environments. Our system incorporates eight motor-driven peltier elements, allowing for the flipping of preheated or cooled elements to the opposite side. In evaluating the Flip-Pelt device, we assess user ability to distinguish between heat/cold sources by their patterns and stiffness, and its impact on enhancing haptic experiences in VR content that involves contact with various thermal sources. Our findings demonstrate that rapid thermal stimulation and congruent pressure feedback provided by Flip-Pelt enhance the recognition accuracy of thermal patterns and the stiffness of virtual objects. These features also improve haptic experiences in VR scenarios through their temporal congruency between tactile and thermal stimuli. Additionally, we discuss the scalability of the Flip-Pelt system to other body parts by proposing design prototypes.



### Hydroptical Thermal Feedback: Spatial Thermal Feedback Using Visible Lights and Water
Authors: Sosuke Ichihashi, Masahiko Inami, Hsin-Ni Ho, Noura Howell

[Link](https://programs.sigchi.org/uist/2024/program/content/170722)

Abstract: We control the temperature of materials in everyday interactions, recognizing temperature's important influence on our bodies, minds, and experiences. However, thermal feedback is an under-explored modality in human-computer interaction partly due to its limited temporal (slow) and spatial (small-area and non-moving) capabilities. We introduce hydroptical thermal feedback, a spatial thermal feedback method that works by applying visible lights on body parts in water. Through physical measurements and psychophysical experiments, our results show: (1) Humans perceive thermal sensations when visible lights are cast on the skin under water, and perceived warmth is greater for lights with shorter wavelengths, (2) temporal capabilities, (3) apparent motion (spatial) of warmth and coolness sensations, and (4) hydroptical thermal feedback can support the perceptual illusion that the water itself is warmer. We propose applications, including virtual reality (VR), shared water experiences, and therapies. Overall, this paper contributes hydroptical thermal feedback as a novel method, empirical results demonstrating its unique capabilities, proposed applications, and design recommendations for using hydroptical thermal feedback. Our method introduces controlled, spatial thermal perceptions to water experiences.




## Break Q&A: LLM: New applications
### VoicePilot: Harnessing LLMs as Speech Interfaces for Assistive Robotics
Authors: Akhil Padmanabha, Jessie Yuan, Janavi Gupta, Zulekha Karachiwalla, Carmel Majidi, Henny Admoni, Zackory Erickson

[Link](https://programs.sigchi.org/uist/2024/program/content/170789)

Abstract: Physically assistive robots present an opportunity to significantly increase the well-being and independence of individuals with motor impairments or other forms of disability who are unable to complete activities of daily living. Speech interfaces, especially ones that utilize Large Language Models (LLMs), can enable individuals to effectively and naturally communicate high-level commands and nuanced preferences to robots. Frameworks for integrating LLMs as interfaces to robots for high level task planning and code generation have been proposed, but fail to incorporate human-centric considerations which are essential while developing assistive interfaces. In this work, we present a framework for incorporating LLMs as speech interfaces for physically assistive robots, constructed iteratively with 3 stages of testing involving a feeding robot, culminating in an evaluation with 11 older adults at an independent living facility. We use both quantitative and qualitative data from the final study to validate our framework and additionally provide design guidelines for using LLMs as speech interfaces for assistive robots. Videos, code, and supporting files are located on our project website\footnote{\url{https://sites.google.com/andrew.cmu.edu/voicepilot/}}



### ComPeer: A Generative Conversational Agent for Proactive Peer Support
Authors: Tianjian Liu, Hongzheng Zhao, Yuheng Liu, Xingbo Wang, Zhenhui Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170845)

Abstract: Conversational Agents (CAs) acting as peer supporters have been widely studied and demonstrated beneficial for people's mental health. However, previous peer support CAs either are user-initiated or follow predefined rules to initiate the conversations, which may discourage users to engage and build relationships with the CAs for long-term benefits. In this paper, we develop ComPeer, a generative CA that can proactively offer adaptive peer support to users. ComPeer leverages large language models to detect and reflect significant events in the dialogue, enabling it to strategically plan the timing and content of proactive care. In addition, ComPeer incorporates peer support strategies, conversation history, and its persona into the generative messages. Our one-week between-subjects study (N=24) demonstrates ComPeer's strength in providing peer support over time and boosting users' engagement compared to a baseline user-initiated CA. We report users' interaction patterns with ComPeer and discuss implications for designing proactive generative agents to promote people's well-being.



### SHAPE-IT: Exploring Text-to-Shape-Display for Generative Shape-Changing Behaviors with LLMs
Authors: Wanli Qian, Chenfeng Gao, Anup Sathya, Ryo Suzuki, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170820)

Abstract: This paper introduces text-to-shape-display, a novel approach to generating dynamic shape changes in pin-based shape displays through natural language commands. By leveraging large language models (LLMs) and AI-chaining, our approach allows users to author shape-changing behaviors on demand through text prompts without programming. We describe the foundational aspects necessary for such a system, including the identification of key generative elements (primitive, animation, and interaction) and design requirements to enhance user interaction, based on formative exploration and iterative design processes. Based on these insights, we develop SHAPE-IT, an LLM-based authoring tool for a 24 x 24 shape display, which translates the user's textual command into executable code and allows for quick exploration through a web-based control interface. We evaluate the effectiveness of SHAPE-IT in two ways: 1) performance evaluation and 2) user evaluation (N= 10). The study conclusions highlight the ability to facilitate rapid ideation of a wide range of shape-changing behaviors with AI. However, the findings also expose accuracy-related challenges and limitations, prompting further exploration into refining the framework for leveraging AI to better suit the unique requirements of shape-changing systems.



### WaitGPT: Monitoring and Steering Conversational LLM Agent in Data Analysis with On-the-Fly Code Visualization
Authors: Liwenhan Xie, Chengbo Zheng, Haijun Xia, Huamin Qu, Chen Zhu-Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/170828)

Abstract: Large language models (LLMs) support data analysis through conversational user interfaces, as exemplified in OpenAI's ChatGPT (formally known as Advanced Data Analysis or Code Interpreter). Essentially, LLMs produce code for accomplishing diverse analysis tasks. However, presenting raw code can obscure the logic and hinder user verification. To empower users with enhanced comprehension and augmented control over analysis conducted by LLMs, we propose a novel approach to transform LLM-generated code into an interactive visual representation. In the approach, users are provided with a clear, step-by-step visualization of the LLM-generated code in real time, allowing them to understand, verify, and modify individual data operations in the analysis. Our design decisions are informed by a formative study (N=8) probing into user practice and challenges. We further developed a prototype named WaitGPT and conducted a user study (N=12) to evaluate its usability and effectiveness. The findings from the user study reveal that WaitGPT facilitates monitoring and steering of data analysis performed by LLMs, enabling participants to enhance error detection and increase their overall confidence in the results.




## Break Q&A: Big to Small Fab
### Don't Mesh Around: Streamlining Manual-Digital Fabrication Workflows with Domain-Specific 3D Scanning
Authors: Ilan Moyer, Sam Bourgault, Devon Frost, Jennifer Jacobs

[Link](https://programs.sigchi.org/uist/2024/program/content/170846)

Abstract: Software-first digital fabrication workflows are often at odds with material-driven approaches to design. Material-driven design is especially critical in manual ceramics, where the craftsperson shapes the form through hands-on engagement. We present the Craft-Aligned Scanner (CAS), a 3D scanning and clay-3D printing system that enables practitioners to design for digital fabrication through traditional pottery techniques. The CAS augments a pottery wheel that has 3D printing capabilities with a precision distance sensor on a vertically oriented linear axis. By increasing the height of the sensor as the wheel turns, we directly synthesize a 3D spiralized toolpath from the geometry of the object on the wheel, enabling the craftsperson to immediately transition from manual fabrication to 3D printing without leaving the tool. We develop new digital fabrication workflows with CAS to augment scanned forms with functional features and add both procedurally and real-time-generated surface textures. CAS demonstrates how 3D printers can support material-first digital fabrication design without foregoing the expressive possibilities of software-based design.



### E-Joint: Fabrication of Large-Scale Interactive Objects Assembled by 3D Printed Conductive Parts with Copper Plated Joints
Authors: Xiaolong Li, Cheng Yao, Shang Shi, Shuyue Feng, Yujie Zhou, Haoye Dong, Shichao Huang, Xueyan Cai, Kecheng Jin, Fangtian Ying, Guanyun Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170987)

Abstract: The advent of conductive thermoplastic filaments and multi-material 3D printing has made it feasible to create interactive 3D printed objects. Yet, challenges arise due to volume constraints of desktop 3D printers and high resistive characteristics of current conductive materials, making the fabrication of large-scale or highly conductive interactive objects can be daunting. We propose E-Joint, a novel fabrication pipeline for 3D printed objects utilizing mortise and tenon joint structures combined with a copper plating process. The segmented pieces and joint structures are customized in software along with integrated circuits. Then electroplate them for enhanced conductivity. We designed four distinct electrified joint structures in experiment and evaluated the practical feasibility and effectiveness of fabricating pipes. By constructing three applications with those structures, we verified the usability of E-Joint in making large-scale interactive objects and show path to a more integrated future for manufacturing.



### MobiPrint: A Mobile 3D Printer for Environment-Scale Design and Fabrication
Authors: Daniel Campos Zamora, Liang He, Jon Froehlich

[Link](https://programs.sigchi.org/uist/2024/program/content/170934)

Abstract: 3D printing is transforming how we customize and create physical objects in engineering, accessibility, and art. However, this technology is still primarily limited to confined working areas and dedicated print beds thereby detaching design and fabrication from real-world environments and making measuring and scaling objects tedious and labor-intensive. In this paper, we present MobiPrint, a prototype mobile fabrication system that combines elements from robotics, architecture, and Human-Computer Interaction (HCI) to enable environment-scale design and fabrication in ad-hoc indoor environments. MobiPrint provides a multi-stage fabrication pipeline: first, the robotic 3D printer automatically scans and maps an indoor space; second, a custom design tool converts the map into an interactive CAD canvas for editing and placing models in the physical world; finally, the MobiPrint robot prints the object directly on the ground at the defined location. Through a "proof-by-demonstration" validation, we highlight our system's potential across different applications, including accessibility, home furnishing, floor signage, and art. We also conduct a technical evaluation to assess MobiPrint’s localization accuracy, ground surface adhesion, payload capacity, and mapping speed. We close with a discussion of open challenges and opportunities for the future of contextualized mobile fabrication.



### StructCurves: Interlocking Block-Based Line Structures
Authors: Zezhou Sun, Devin Balkcom, Emily Whiting

[Link](https://programs.sigchi.org/uist/2024/program/content/171006)

Abstract: We present a new class of curved block-based line structures whose component chains are flexible when separated, and provably rigid when assembled together into an interlocking double chain. The joints are inspired by traditional zippers, where a binding fabric or mesh connects individual teeth.
Unlike traditional zippers, the joint design produces a rigid interlock with programmable curvature. This allows fairly strong curved structures to be built out of easily stored flexible chains. 
In this paper, we introduce a pipeline for generating these curved structures using a novel block design template based on revolute joints. 
Mesh embedded in these structures maintains block spacing and assembly order. We evaluate the rigidity of the curved structures through mechanical performance testing and demonstrate several applications. 




## Break Q&A: Shared Spaces
### BlendScape: Enabling End-User Customization of Video-Conferencing Environments through Generative AI
HONORABLE_MENTION

Authors: Shwetha Rajaram, Nels Numan, Bala Kumaravel, Nicolai Marquardt, Andrew Wilson

[Link](https://programs.sigchi.org/uist/2024/program/content/170854)

Abstract: Today’s video-conferencing tools support a rich range of professional and social activities, but their generic meeting environments cannot be dynamically adapted to align with distributed collaborators’ needs. To enable end-user customization, we developed BlendScape, a rendering and composition system for video-conferencing participants to tailor environments to their meeting context by leveraging AI image generation techniques. BlendScape supports flexible representations of task spaces by blending users’ physical or digital backgrounds into unified environments and implements multimodal interaction techniques to steer the generation. Through an exploratory study with 15 end-users, we investigated whether and how they would find value in using generative AI to customize video-conferencing environments. Participants envisioned using a system like BlendScape to facilitate collaborative activities in the future, but required further controls to mitigate distracting or unrealistic visual elements. We implemented scenarios to demonstrate BlendScape's expressiveness for supporting environment design strategies from prior work and propose composition techniques to improve the quality of environments.



### SpaceBlender: Creating Context-Rich Collaborative Spaces Through Generative 3D Scene Blending
Authors: Nels Numan, Shwetha Rajaram, Bala Kumaravel, Nicolai Marquardt, Andrew Wilson

[Link](https://programs.sigchi.org/uist/2024/program/content/170843)

Abstract: There is increased interest in using generative AI to create 3D spaces for virtual reality (VR) applications. However, today’s models produce artificial environments, falling short of supporting collaborative tasks that benefit from incorporating the user's physical context. To generate environments that support VR telepresence, we introduce SpaceBlender, a novel pipeline that utilizes generative AI techniques to blend users' physical surroundings into unified virtual spaces. This pipeline transforms user-provided 2D images into context-rich 3D environments through an iterative process consisting of depth estimation, mesh alignment, and diffusion-based space completion guided by geometric priors and adaptive text prompts. In a preliminary within-subjects study, where 20 participants performed a collaborative VR affinity diagramming task in pairs, we compared SpaceBlender with a generic virtual environment and a state-of-the-art scene generation framework, evaluating its ability to create virtual spaces suitable for collaboration. Participants appreciated the enhanced familiarity and context provided by SpaceBlender but also noted complexities in the generative environments that could detract from task focus. Drawing on participant feedback, we propose directions for improving the pipeline and discuss the value and design of blended spaces for different scenarios.



### MyWebstrates: Webstrates as Local-first Software
Authors: Clemens Klokmose, James Eagan, Peter van Hardenberg

[Link](https://programs.sigchi.org/uist/2024/program/content/170812)

Abstract: Webstrates are web substrates, a practical realization of shareable dynamic media under which distributability, shareability, and malleability are fundamental software principles. Webstrates blur the distinction between application and document in a way that enables users to share, repurpose, and refit software across a variety of domains, but its reliance on a central server constrains its use; it is at odds with personal and collective control of data; and limits applications to the web. We extend the fundamental principles to include interoperability and sovereignty over data and propose MyWebstrates, an implementation of Webstrates on top of a new, lower-level substrate for synchronization built around local-first software principles. MyWebstrates registers itself in the user’s browser and function as a piece of local software that can selectively synchronise data over sync servers or peer-to-peer connections. We show how MyWebstrates extends Webstrates to enable offline collaborative use, interoperate between Webstrates on non-web technologies such as Unity, and maintain personal and collective sovereignty over data. We demonstrate how this enables new types of applications of Webstrates and discuss limitations of this approach and new challenges that it reveals.



### SituationAdapt: Contextual UI Optimization in Mixed Reality with Situation Awareness via LLM Reasoning
Authors: Zhipeng Li, Christoph Gebhardt, Yves Inglin, Nicolas Steck, Paul Streli, Christian Holz

[Link](https://programs.sigchi.org/uist/2024/program/content/170856)

Abstract: Mixed Reality is increasingly used in mobile settings beyond controlled home and office spaces. This mobility introduces the need for user interface layouts that adapt to varying contexts. However, existing adaptive systems are designed only for static environments. In this paper, we introduce SituationAdapt, a system that adjusts Mixed Reality UIs to real-world surroundings by considering environmental and social cues in shared settings. Our system consists of perception, reasoning, and optimization modules for UI adaptation. Our perception module identifies objects and individuals around the user, while our reasoning module leverages a Vision-and-Language Model to assess the placement of interactive UI elements. This ensures that adapted layouts do not obstruct relevant environmental cues or interfere with social norms. Our optimization module then generates Mixed Reality interfaces that account for these considerations as well as temporal constraints The evaluation of SituationAdapt is two-fold: We first validate our reasoning component’s capability in assessing UI contexts comparable to human expert users. In an online user study, we then established our system’s capability of producing context-aware MR layouts, where it outperformed adaptive methods from previous work. We further demonstrate the versatility and applicability of SituationAdapt with a set of application scenarios.



### Desk2Desk: Optimization-based Mixed Reality Workspace Integration for Remote Side-by-side Collaboration
Authors: Ludwig Sidenmark, Tianyu Zhang, Leen Al Lababidi, Jiannan Li, Tovi Grossman

[Link](https://programs.sigchi.org/uist/2024/program/content/170830)

Abstract: Mixed Reality enables hybrid workspaces where physical and virtual monitors are adaptively created and moved to suit the current environment and needs. However, in shared settings, individual users’ workspaces are rarely aligned and can vary significantly in the number of monitors, available physical space, and workspace layout, creating inconsistencies between workspaces which may cause confusion and reduce collaboration. We present Desk2Desk, an optimization-based approach for remote collaboration in which the hybrid workspaces of two collaborators are fully integrated to enable immersive side-by-side collaboration. The optimization adjusts each user’s workspace in layout and number of shared monitors and creates a mapping between workspaces to handle inconsistencies between workspaces due to physical constraints (e.g. physical monitors). We show in a user study how our system adaptively merges dissimilar physical workspaces to enable immersive side-by-side collaboration, and demonstrate how an optimization-based approach can effectively address dissimilar physical layouts.





## Break Q&A: Learning to Learn
### Patterns of Hypertext-Augmented Sensemaking
Authors: Siyi Zhu, Robert Haisfield, Brendan Langen, Joel Chan

[Link](https://programs.sigchi.org/uist/2024/program/content/170882)

Abstract: The early days of HCI were marked by bold visions of hypertext as a transformative medium for augmented sensemaking, exemplified in systems like Memex, Xanadu, and NoteCards. Today, however, hypertext is often disconnected from discussions of the future of sensemaking. In this paper, we investigate how the recent resurgence in hypertext ``tools for thought'' might point to new directions for hypertext-augmented sensemaking. Drawing on detailed analyses of guided tours with 23 scholars, we describe hypertext-augmented use patterns for dealing with the core problem of revisiting and reusing existing/past ideas during scholarly sensemaking. We then discuss how these use patterns validate and extend existing knowledge of hypertext design patterns for sensemaking, and point to new design opportunities for augmented sensemaking.



### Augmented Physics: Creating Interactive and Embedded Physics Simulations from Static Textbook Diagrams
BEST_PAPER

Authors: Aditya Gunturu, Yi Wen, Nandi Zhang, Jarin Thundathil, Rubaiat Habib Kazi, Ryo Suzuki

[Link](https://programs.sigchi.org/uist/2024/program/content/170907)

Abstract: We introduce Augmented Physics, a machine learning-integrated authoring tool designed for creating embedded interactive physics simulations from static textbook diagrams. Leveraging recent advancements in computer vision, such as Segment Anything and Multi-modal LLMs, our web-based system enables users to semi-automatically extract diagrams from physics textbooks and generate interactive simulations based on the extracted content. These interactive diagrams are seamlessly integrated into scanned textbook pages, facilitating interactive and personalized learning experiences across various physics concepts, such as optics, circuits, and kinematics. Drawing from an elicitation study with seven physics instructors, we explore four key augmentation strategies: 1) augmented experiments, 2) animated diagrams, 3) bi-directional binding, and 4) parameter visualization. We evaluate our system through technical evaluation, a usability study (N=12), and expert interviews (N=12). Study findings suggest that our system can facilitate more engaging and personalized learning experiences in physics education.



### Qlarify: Recursively Expandable Abstracts for Dynamic Information Retrieval over Scientific Papers
Authors: Raymond Fok, Joseph Chee Chang, Tal August, Amy Zhang, Daniel Weld

[Link](https://programs.sigchi.org/uist/2024/program/content/170964)

Abstract: Navigating the vast scientific literature often starts with browsing a paper’s abstract. However, when a reader seeks additional information, not present in the abstract, they face a costly cognitive chasm during their dive into the full text. To bridge this gap, we introduce recursively expandable abstracts, a novel interaction paradigm that dynamically expands abstracts by progressively incorporating additional information from the papers’ full text. This lightweight interaction allows scholars to specify their information needs by quickly brushing over the abstract or selecting AI-suggested expandable entities. Relevant information is synthesized using a retrieval-augmented generation approach, presented as a fluid, threaded expansion of the abstract, and made efficiently verifiable via attribution to relevant source-passages in the paper. Through a series of user studies, we demonstrate the utility of recursively expandable abstracts and identify future opportunities to support low-effort and just-in-time exploration of long-form information contexts through LLM-powered interactions.



### LessonPlanner: Assisting Novice Teachers to Prepare Pedagogy-Driven Lesson Plans with Large Language Models
Authors: Haoxiang Fan, Guanzheng Chen, Xingbo Wang, Zhenhui Peng

[Link](https://programs.sigchi.org/uist/2024/program/content/170883)

Abstract: Preparing a lesson plan, e.g., a detailed road map with strategies and materials for instructing a 90-minute class, is beneficial yet challenging for novice teachers. Large language models (LLMs) can ease this process by generating adaptive content for lesson plans, which would otherwise require teachers to create from scratch or search existing resources. In this work, we first conduct a formative study with six novice teachers to understand their needs for support of preparing lesson plans with LLMs. Then, we develop LessonPlanner that assists users to interactively construct lesson plans with adaptive LLM-generated content based on Gagne's nine events. Our within-subjects study (N=12) shows that compared to the baseline ChatGPT interface, LessonPlanner can significantly improve the quality of outcome lesson plans and ease users' workload in the preparation process. Our expert interviews (N=6) further demonstrate LessonPlanner's usefulness in suggesting effective teaching strategies and meaningful educational resources. We discuss concerns on and design considerations for supporting teaching activities with LLMs.




## Break Q&A: Generating Visuals
### ShadowMagic: Designing Human-AI Collaborative Support for Comic Professionals’ Shadowing
Authors: Amrita Ganguly, Chuan Yan, John Chung, Tong Sun, YOON KIHEON, Yotam Gingold, Sungsoo Ray Hong

[Link](https://programs.sigchi.org/uist/2024/program/content/170726)

Abstract: Shadowing allows artists to convey realistic volume and emotion of characters in comic colorization. While AI technologies have the potential to improve professionals’ shadowing experience, current practice is manual and time-consuming. To understand how we can improve their shadowing experience, we conducted interviews with 5 professionals. We found that professionals’ level of engagement can vary depending on semantics, such as characters’ faces or hair. We also found they spent time on shadow “landscaping”—deciding where to place large shadow regions to create a realistic volumetric presentation while the final results can vary dramatically depending on their “staging” and “attention guiding” needs. We discovered they would accept AI suggestions for less engaging semantic parts or landscaping, while needing the capability to adjust details. Based on our observations, we developed ShadowMagic, which (1) generates AI-driven shadows based on commonly used light directions, (2) enables users to selectively choose results depending on semantics, and (3) allows users to complete shadow areas themselves for further perfection. Through a summative evaluation with 5 professionals, we found that they were significantly more satisfied with our AI-driven results compared to a baseline. We also found that ShadowMagic’s “step by step” workflow helps participants more easily adopt AI-driven results. We conclude by providing implications.



### What's the Game, then? Opportunities and Challenges for Runtime Behavior Generation
BEST_PAPER

Authors: Nicholas Jennings, Han Wang, Isabel Li, James Smith, Bjoern Hartmann

[Link](https://programs.sigchi.org/uist/2024/program/content/170924)

Abstract: Procedural content generation (PCG), the process of algorithmically creating game components instead of manually, has been a common tool of game development for decades. Recent advances in large language models (LLMs) enable the generation of game behaviors based on player input at runtime. Such code generation brings with it the possibility of entirely new gameplay interactions that may be difficult to integrate with typical game development workflows. We explore these implications through GROMIT, a novel LLM-based runtime behavior generation system for Unity. When triggered by a player action, GROMIT generates a relevant behavior which is compiled without developer intervention and incorporated into the game. We create three demonstration scenarios with GROMIT to investigate how such a technology might be used in game development. In a system evaluation we find that our implementation is able to produce behaviors that result in significant downstream impacts to gameplay. We then conduct an interview study with n=13 game developers using GROMIT as a probe to elicit their current opinion on runtime behavior generation tools, and enumerate the specific themes curtailing the wider use of such tools. We find that the main themes of concern are quality considerations, community expectations, and fit with developer workflows, and that several of the subthemes are unique to runtime behavior generation specifically. We outline a future work agenda to address these concerns, including the need for additional guardrail systems for behavior generation.



### StyleFactory: Towards Better Style Alignment in Image Creation through Style-Strength-Based Control and Evaluation
Authors: Mingxu Zhou, Dengming Zhang, Weitao You, Ziqi Yu, Yifei Wu, Chenghao Pan, Huiting Liu, Tianyu Lao, Pei Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170929)

Abstract: Generative AI models have been widely used for image creation. However, generating images that are well-aligned with users' personal styles on aesthetic features (e.g., color and texture) can be challenging due to the poor style expression and interpretation between humans and models. Through a formative study, we observed that participants showed a clear subjective perception of the desired style and variations in its strength, which directly inspired us to develop style-strength-based control and evaluation. Building on this, we present StyleFactory, an interactive system that helps users achieve style alignment. Our interface enables users to rank images based on their strengths in the desired style and visualizes the strength distribution of other images in that style from the model's perspective. In this way, users can evaluate the understanding gap between themselves and the model, and define well-aligned personal styles for image creation through targeted iterations. Our technical evaluation and user study demonstrate that StyleFactory accurately generates images in specific styles, effectively facilitates style alignment in image creation workflow, stimulates creativity, and enhances the user experience in human-AI interactions.



### AutoSpark: Supporting Automobile Appearance Design Ideation with Kansei Engineering and Generative AI
Authors: Liuqing Chen, Qianzhi Jing, Yixin Tsang, Qianyi Wang, Ruocong Liu, Duowei Xia, Yunzhan Zhou, Lingyun Sun

[Link](https://programs.sigchi.org/uist/2024/program/content/170878)

Abstract: Rapid creation of novel product appearance designs that align with consumer emotional requirements poses a significant challenge. Text-to-image models, with their excellent image generation capabilities, have demonstrated potential in providing inspiration to designers. However, designers still encounter issues including aligning emotional needs, expressing design intentions, and comprehending generated outcomes in practical applications. To address these challenges, we introduce AutoSpark, an interactive system that integrates Kansei Engineering and generative AI to provide creativity support for designers in creating automobile appearance designs that meet emotional needs. AutoSpark employs a Kansei Engineering engine powered by generative AI and a semantic network to assist designers in emotional need alignment, design intention expression, and prompt crafting. It also facilitates designers' understanding and iteration of generated results through fine-grained image-image similarity comparisons and text-image relevance assessments. The design-thinking map within its interface aids in managing the design process. Our user study indicates that AutoSpark effectively aids designers in producing designs that are more aligned with emotional needs and of higher quality compared to a baseline system, while also enhancing the designers' experience in the human-AI co-creation process.




## Break Q&A: Hacking Perception
### Predicting the Limits: Tailoring Unnoticeable Hand Redirection Offsets in Virtual Reality to Individuals’ Perceptual Boundaries
Authors: Martin Feick, Kora Regitz, Lukas Gehrke, André Zenner, Anthony Tang, Tobias Jungbluth, Maurice Rekrut, Antonio Krüger

[Link](https://programs.sigchi.org/uist/2024/program/content/171017)

Abstract: Many illusion and interaction techniques in Virtual Reality (VR) rely on Hand Redirection (HR), which has proved to be effective as long as the introduced offsets between the position of the real and virtual hand do not noticeably disturb the user experience. Yet calibrating HR offsets is a tedious and time-consuming process involving psychophysical experimentation, and the resulting thresholds are known to be affected by many variables---limiting HR's practical utility. As a result, there is a clear need for alternative methods that allow tailoring HR to the perceptual boundaries of individual users. We conducted an experiment with 18 participants combining movement, eye gaze and EEG data to detect HR offsets Below, At, and Above individuals' detection thresholds. Our results suggest that we can distinguish HR At and Above from no HR. Our exploration provides a promising new direction with potentially strong implications for the broad field of VR illusions.



### Modulating Heart Activity and Task Performance using Haptic Heartbeat Feedback: A Study Across Four Body Placements
Authors: Andreia Valente, Dajin Lee, Seungmoon Choi, Mark Billinghurst, Augusto Esteves

[Link](https://programs.sigchi.org/uist/2024/program/content/170839)

Abstract: This paper explores the impact of vibrotactile haptic feedback on heart activity when the feedback is provided at four different body locations (chest, wrist, neck, and ankle) and with two feedback rates (50 bpm and 110 bpm). A user study found that the neck placement resulted in higher heart rates and lower heart rate variability, and higher frequencies correlated with increased heart rates and decreased heart rate variability. The chest was preferred in self-reported metrics, and neck placement was perceived as less satisfying, harmonious, and immersive. This research contributes to understanding the interplay between psychological experiences and physiological responses when using haptic biofeedback resembling real body signals. 



### Augmented Breathing via Thermal Feedback in the Nose
Authors: Jas Brooks, Alex Mazursky, Janice Hixon, Pedro Lopes

[Link](https://programs.sigchi.org/uist/2024/program/content/170728)

Abstract: We propose, engineer, and study a novel method to augment the feeling of breathing—enabling interactive applications to let users feel like they are inhaling more/less air (perceived nasal airflow). We achieve this effect by cooling or heating the nose in sync with the user’s inhalation. Our illusion builds on the physiology of breathing: we perceive our breath predominantly through the cooling of our nasal cavities during inhalation. This is why breathing in a “fresh” cold environment feels easier than in a “stuffy” hot environment, even when the inhaled volume is the same. Our psychophysical study confirmed that our in-nose temperature stimulation significantly influenced breathing perception in both directions: making it feel harder & easier to breathe. Further, we found that ~90% of the trials were described as a change in perceived airflow/breathing, while only ~8% as temperature. Following, we engineered a compact device worn across the septum that uses Peltier elements. We illustrate the potential of this augmented breathing in interactive contexts, such as for virtual reality (e.g., rendering ease of breathing crisp air or difficulty breathing with a deteriorated gas mask) and everyday interactions (e.g., in combination with a relaxation application or to alleviate the perceived breathing resistance when wearing a mask).



### Thermal In Motion: Designing Thermal Flow Illusions with Tactile and Thermal Interaction
Authors: Yatharth Singhal, Daniel Honrales, Haokun Wang, Jin Ryong Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170896)

Abstract: This study presents a novel method for creating moving thermal sensations by integrating the thermal referral illusion with tactile motion. Conducted through three experiments on human forearms, the first experiment examined the impact of temperature and thermal actuator placement on perceived thermal motion, finding the clearest perception with a centrally positioned actuator under both hot and cold conditions. The second experiment identified the speed thresholds of perceived thermal motion, revealing a wider detectable range in hot conditions (1.8 cm/s to 9.5cm/s) compared to cold conditions (2.4cm/s to 5.0cm/s). Finally, we integrated our approach into virtual reality (VR) to assess its feasibility through two interaction scenarios. Our results shed light on the comprehension of thermal perception and its integration with tactile cues, promising significant advancements in incorporating thermal motion into diverse thermal interfaces for immersive VR experiences.




## Break Q&A: Beyond mobile
### picoRing: battery-free rings for subtle thumb-to-index input
Authors: Ryo Takahashi, Eric Whitmire, Roger Boldu, Shiu Ng, Wolf Kienzle, Hrvoje Benko

[Link](https://programs.sigchi.org/uist/2024/program/content/170844)

Abstract: Smart rings for subtle, reliable finger input offer an attractive path for ubiquitous interaction with wearable computing platforms. 
However, compared to ordinary rings worn for cultural or fashion reasons, smart rings are much bulkier and less comfortable, largely due to the space required for a battery, which also limits the space available for sensors.
This paper presents picoRing, a flexible sensing architecture that enables a variety of battery-free smart rings paired with a wristband. 
By inductively connecting a wristband-based sensitive reader coil with a ring-based fully-passive sensor coil, picoRing enables the wristband to stably detect the passive response from the ring via a weak inductive coupling. 
We demonstrate four different rings that support thumb-to-finger interactions like pressing, sliding, or scrolling.
When users perform these interactions, the corresponding ring converts each input into a unique passive response through a network of passive switches.
Combining the coil-based sensitive readout with the fully-passive ring design enables a tiny ring that weighs as little as 1.5 g and achieves a 13 cm stable readout despite finger bending, and proximity to metal.



### WatchLink: Enhancing Smartwatches with Sensor Add-Ons via ECG Interface
Authors: Anandghan Waghmare, Ishan Chatterjee, Vikram Iyer, Shwetak Patel

[Link](https://programs.sigchi.org/uist/2024/program/content/170782)

Abstract: We introduce a low-power communication method that lets smartwatches leverage existing electrocardiogram (ECG) hardware as a data communication interface.  Our unique approach enables the connection of external, inexpensive, and low-power "add-on" sensors to the smartwatch, expanding its functionalities. These sensors cater to specialized user needs beyond those offered by pre-built sensor suites, at a fraction of the cost and power of traditional communication protocols, including Bluetooth Low Energy. To demonstrate the feasibility of our approach, we conduct a series of exploratory and evaluative tests to characterize the ECG interface as a communication channel on commercial smartwatches. We design a simple transmission scheme using commodity components, demonstrating cost and power benefits. Further, we build and test a suite of add-on sensors, including UV light, body temperature, buttons, and breath alcohol, all of which achieved testing objectives at low material cost and power usage. This research paves the way for personalized and user-centric wearables by offering a cost-effective solution to expand their functionalities.




### PrISM-Observer: Intervention Agent to Help Users Perform Everyday Procedures Sensed using a Smartwatch
Authors: Riku Arakawa, Hiromu Yakura, Mayank Goel

[Link](https://programs.sigchi.org/uist/2024/program/content/170914)

Abstract: We routinely perform procedures (such as cooking) that include a set of atomic steps. Often, inadvertent omission or misordering of a single step can lead to serious consequences, especially for those experiencing cognitive challenges such as dementia. This paper introduces PrISM-Observer, a smartwatch-based, context-aware, real-time intervention system designed to support daily tasks by preventing errors. Unlike traditional systems that require users to seek out information, the agent observes user actions and intervenes proactively. This capability is enabled by the agent's ability to continuously update its belief in the user's behavior in real-time through multimodal sensing and forecast optimal intervention moments and methods. We first validated the steps-tracking performance of our framework through evaluations across three datasets with different complexities. Then, we implemented a real-time agent system using a smartwatch and conducted a user study in a cooking task scenario. The system generated helpful interventions, and we gained positive feedback from the participants. The general applicability of PrISM-Observer to daily tasks promises broad applications, for instance, including support for users requiring more involved interventions, such as people with dementia or post-surgical patients.




## Break Q&A: New realities
### SIM2VR: Towards Automated Biomechanical Testing in VR
Authors: Florian Fischer, Aleksi Ikkala, Markus Klar, Arthur Fleig, Miroslav Bachinski, Roderick Murray-Smith, Perttu Hämäläinen, Antti Oulasvirta, Jörg Müller

[Link](https://programs.sigchi.org/uist/2024/program/content/170989)

Abstract: Automated biomechanical testing has great potential for the development of VR applications, as initial insights into user behaviour can be gained in silico early in the design process.
In particular, it allows prediction of user movements and ergonomic variables, such as fatigue, prior to conducting user studies.
However, there is a fundamental disconnect between simulators hosting state-of-the-art biomechanical user models and simulators used to develop and run VR applications. 
Existing user simulators often struggle to capture the intricacies of real-world VR applications, reducing ecological validity of user predictions.
In this paper, we introduce SIM2VR, a system that aligns user simulation with a given VR application by establishing a continuous closed loop between the two processes.
This, for the first time, enables training simulated users directly in the same VR application that real users interact with.
We demonstrate that SIM2VR can predict differences in user performance, ergonomics and strategies in a fast-paced, dynamic arcade game. In order to expand the scope of automated biomechanical testing beyond simple visuomotor tasks, advances in cognitive models and reward function design will be needed.



### Hands-on, Hands-off: Gaze-Assisted Bimanual 3D Interaction
Authors: Mathias Lystbæk, Thorbjørn Mikkelsen, Roland Krisztandl, Eric Gonzalez, Mar Gonzalez-Franco, Hans Gellersen, Ken Pfeuffer

[Link](https://programs.sigchi.org/uist/2024/program/content/171002)

Abstract: Extended Reality (XR) systems with hand-tracking support direct manipulation of objects with both hands. A common interaction in this context is for the non-dominant hand (NDH) to orient an object for input by the dominant hand (DH). We explore bimanual interaction with gaze through three new modes of interaction where the input of the NDH, DH, or both hands is indirect based on Gaze+Pinch. These modes enable a new dynamic interplay between our hands, allowing flexible alternation between and pairing of complementary operations. Through applications, we demonstrate several use cases in the context of 3D modelling, where users exploit occlusion-free, low-effort, and fluid two-handed manipulation. To gain a deeper understanding of each mode, we present a user study on an asymmetric rotate-translate task. Most participants preferred indirect input with both hands for lower physical effort, without a penalty on user performance. Otherwise, they preferred modes where the NDH oriented the object directly, supporting preshaping of the hand, which is more challenging with indirect gestures. The insights gained are of relevance for the design of XR interfaces that aim to leverage eye and hand input in tandem.



### Pro-Tact: Hierarchical Synthesis of Proprioception and Tactile Exploration for Eyes-Free Ray Pointing on Out-of-View VR Menus
Authors: Yeonsu Kim, Jisu Yim, Kyunghwan Kim, Yohan Yun, Geehyuk Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170805)

Abstract: We introduce Pro-Tact, a novel eyes-free pointing technique for interacting with out-of-view (OoV) VR menus. This technique combines rapid rough pointing using proprioception with fine-grain adjustments through tactile exploration, enabling menu interaction without visual attention. Our user study demonstrated that Pro-Tact allows users to select menu items accurately (95% accuracy for 54 items) in an eyes-free manner, with reduced fatigue and sickness compared to eyes-engaged interaction. Additionally, we observed that participants voluntarily interacted with OoV menus eyes-free when Pro-Tact's tactile feedback was provided in practical VR application usage contexts. This research contributes by introducing the novel interaction technique, Pro-Tact, and quantitatively evaluating its benefits in terms of performance, user experience, and user preference in OoV menu interactions.



### GradualReality: Enhancing Physical Object Interaction in Virtual Reality via Interaction State-Aware Blending
Authors: HyunA Seo, Juheon Yi, Rajesh Balan, Youngki Lee

[Link](https://programs.sigchi.org/uist/2024/program/content/170920)

Abstract: We present GradualReality, a novel interface enabling a Cross Reality experience that includes gradual interaction with physical objects in a virtual environment and supports both presence and usability. Daily Cross Reality interaction is challenging as the user's physical object interaction state is continuously changing over time, causing their attention to frequently shift between the virtual and physical worlds. As such, presence in the virtual environment and seamless usability for interacting with physical objects should be maintained at a high level. To address this issue, we present an Interaction State-Aware Blending approach that (i) balances immersion and interaction capability and (ii) provides a fine-grained, gradual transition between virtual and physical worlds. The key idea includes categorizing the flow of physical object interaction into multiple states and designing novel blending methods that offer optimal presence and sufficient physical awareness at each state. We performed extensive user studies and interviews with a working prototype and demonstrated that GradualReality provides better Cross Reality experiences compared to baselines.



### StegoType: Surface Typing from Egocentric Cameras
Authors: Mark Richardson, Fadi Botros, Yangyang Shi, Pinhao Guo, Bradford Snow, Linguang Zhang, Jingming Dong, Keith Vertanen, Shugao Ma, Robert Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170853)

Abstract: Text input is a critical component of any general purpose computing system, yet efficient and natural text input remains a challenge in AR and VR. Headset based hand-tracking has recently become pervasive among consumer VR devices and affords the opportunity to enable touch typing on virtual keyboards. We present an approach for decoding touch typing on uninstrumented flat surfaces using only egocentric camera-based hand-tracking as input. While egocentric hand-tracking accuracy is limited by issues like self occlusion and image fidelity, we show that a sufficiently diverse training set of hand motions paired with typed text can enable a deep learning model to extract signal from this noisy input. 
Furthermore, by carefully designing a closed-loop data collection process, we can train an end-to-end text decoder that accounts for natural sloppy typing on virtual keyboards.  
We evaluate our work with a user study (n=18) showing a mean online throughput of 42.4 WPM with an uncorrected error rate (UER) of 7% with our method compared to a physical keyboard baseline of 74.5 WPM at 0.8% UER, showing progress towards unlocking productivity and high throughput use cases in AR/VR.



### Eye-Hand Movement of Objects in Near Space Extended Reality
Authors: Uta Wagner, Andreas Asferg Jacobsen, Tiare Feuchtner, Hans Gellersen, Ken Pfeuffer

[Link](https://programs.sigchi.org/uist/2024/program/content/170771)

Abstract: Hand-tracking in Extended Reality (XR) enables moving objects in near space with direct hand gestures, to pick, drag and drop objects in 3D. In this work, we investigate the use of eye-tracking to reduce the effort involved in this interaction. As the eyes naturally look ahead to the target for a drag operation, the principal idea is to map the translation of the object in the image plane to gaze, such that the hand only needs to control the depth component of the operation. We have implemented four techniques that explore two factors: the use of gaze only to move objects in X-Y vs.\ extra refinement by hand, and the use of hand input in 
 the Z axis to directly move objects vs.\ indirectly via a transfer function. We compared all four techniques in a user study (N=24) against baselines of direct and indirect hand input. We detail user performance, effort and experience trade-offs and show that all eye-hand techniques significantly reduce physical effort over direct gestures, pointing toward effortless drag-and-drop for XR environments.




## Break Q&A: Contextual Augmentations
### StreetNav: Leveraging Street Cameras to Support Precise Outdoor Navigation for Blind Pedestrians
Authors: Gaurav Jain, Basel Hindi, Zihao Zhang, Koushik Srinivasula, Mingyu Xie, Mahshid Ghasemi, Daniel Weiner, Sophie Ana Paris, Xin Yi Therese Xu, Michael Malcolm, Mehmet Kerem Turkcan, Javad Ghaderi, Zoran Kostic, Gil Zussman, Brian Smith

[Link](https://programs.sigchi.org/uist/2024/program/content/171003)

Abstract: Blind and low-vision (BLV) people rely on GPS-based systems for outdoor navigation. GPS's inaccuracy, however, causes them to veer off track, run into obstacles, and struggle to reach precise destinations. While prior work has made precise navigation possible indoors via hardware installations, enabling this outdoors remains a challenge. Interestingly, many outdoor environments are already instrumented with hardware such as street cameras. In this work, we explore the idea of repurposing existing street cameras for outdoor navigation. Our community-driven approach considers both technical and sociotechnical concerns through engagements with various stakeholders: BLV users, residents, business owners, and Community Board leadership. The resulting system, StreetNav, processes a camera's video feed using computer vision and gives BLV pedestrians real-time navigation assistance. Our evaluations show that StreetNav guides users more precisely than GPS, but its technical performance is sensitive to environmental occlusions and distance from the camera. We discuss future implications for deploying such systems at scale.



### WorldScribe: Towards Context-Aware Live Visual Descriptions
BEST_PAPER

Authors: Ruei-Che Chang, Yuxuan Liu, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170940)

Abstract: Automated live visual descriptions can aid blind people in understanding their surroundings with autonomy and independence. However, providing descriptions that are rich, contextual, and just-in-time has been a long-standing challenge in accessibility. In this work, we develop WorldScribe, a system that generates automated live real-world visual descriptions that are customizable and adaptive to users' contexts: (i) WorldScribe's descriptions are tailored to users' intents and prioritized based on semantic relevance. (ii) WorldScribe is adaptive to visual contexts, e.g., providing consecutively succinct descriptions for dynamic scenes, while presenting longer and detailed ones for stable settings. (iii) WorldScribe is adaptive to sound contexts, e.g., increasing volume in noisy environments, or pausing when conversations start. Powered by a suite of vision, language, and sound recognition models, WorldScribe introduces a description generation pipeline that balances the tradeoffs between their richness and latency to support real-time use. The design of WorldScribe is informed by prior work on providing visual descriptions and a formative study with blind participants. Our user study and subsequent pipeline evaluation show that WorldScribe can provide real-time and fairly accurate visual descriptions to facilitate environment understanding that is adaptive and customized to users' contexts. Finally, we discuss the implications and further steps toward making live visual descriptions more context-aware and humanized.



### CookAR: Affordance Augmentations in Wearable AR to Support Kitchen Tool Interactions for People with Low Vision
Authors: Jaewook Lee, Andrew Tjahjadi, Jiho Kim, Junpu Yu, Minji Park, Jiawen Zhang, Jon Froehlich, Yapeng Tian, Yuhang Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/170874)

Abstract: Cooking is a central activity of daily living, supporting independence as well as mental and physical health. However, prior work has highlighted key barriers for people with low vision (LV) to cook, particularly around safely interacting with tools, such as sharp knives or hot pans. Drawing on recent advancements in computer vision (CV), we present CookAR, a head-mounted AR system with real-time object affordance augmentations to support safe and efficient interactions with kitchen tools. To design and implement CookAR, we collected and annotated the first egocentric dataset of kitchen tool affordances, fine-tuned an affordance segmentation model, and developed an AR system with a stereo camera to generate visual augmentations. To validate CookAR, we conducted a technical evaluation of our fine-tuned model as well as a qualitative lab study with 10 LV participants for suitable augmentation design. Our technical evaluation demonstrates that our model outperforms the baseline on our tool affordance dataset, while our user study indicates a preference for affordance augmentations over the traditional whole object augmentations.



### DesignChecker: Visual Design Support for Blind and Low Vision Web Developers
Authors: Mina Huh, Amy Pavel

[Link](https://programs.sigchi.org/uist/2024/program/content/170953)

Abstract: Blind and low vision (BLV) developers create websites to share knowledge and showcase their work. A well-designed website can engage audiences and deliver information effectively, yet it remains challenging for BLV developers to review their web designs. We conducted interviews with BLV developers (N=9) and analyzed 20 websites created by BLV developers. BLV developers created highly accessible websites but wanted to assess the usability of their websites for sighted users and follow the design standards of other websites. They also encountered challenges using screen readers to identify illegible text, misaligned elements, and inharmonious colors. We present DesignChecker, a browser extension that helps BLV developers improve their web designs. With DesignChecker, users can assess their current design by comparing it to visual design guidelines, a reference website of their choice, or a set of similar websites. DesignChecker also identifies the specific HTML elements that violate design guidelines and suggests CSS changes for improvements. Our user study participants (N=8) recognized more visual design errors than using their typical workflow and expressed enthusiasm about using DesignChecker in the future.




## Break Q&A: Machine Learning for User Interfaces
### UIClip: A Data-driven Model for Assessing User Interface Design
Authors: Jason Wu, Yi-Hao Peng, Xin Yue Li, Amanda Swearngin, Jeffrey Bigham, Jeffrey Nichols

[Link](https://programs.sigchi.org/uist/2024/program/content/170950)

Abstract: User interface (UI) design is a difficult yet important task for ensuring the usability, accessibility, and aesthetic qualities of applications. In our paper, we develop a machine-learned model, UIClip, for assessing the design quality and visual relevance of a UI given its screenshot and natural language description. To train UIClip, we used a combination of automated crawling, synthetic augmentation, and human ratings to construct a large-scale dataset of UIs, collated by description and ranked by design quality. Through training on the dataset, UIClip implicitly learns properties of good and bad designs by (i) assigning a numerical score that represents a UI design's relevance and quality and (ii) providing design suggestions. In an evaluation that compared the outputs of UIClip and other baselines to UIs rated by 12 human designers, we found that UIClip achieved the highest agreement with ground-truth rankings. Finally, we present three example applications that demonstrate how UIClip can facilitate downstream applications that rely on instantaneous assessment of UI design quality: (i) UI code generation, (ii) UI design tips generation, and (iii) quality-aware UI example search.



### UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset
Authors: Peitong Duan, Chin-Yi Cheng, Gang Li, Bjoern Hartmann, Yang Li

[Link](https://programs.sigchi.org/uist/2024/program/content/170823)

Abstract: Automated UI evaluation can be beneficial for the design process; for example, to compare different UI designs, or conduct automated heuristic evaluation. LLM-based UI evaluation, in particular, holds the promise of generalizability to a wide variety of UI types and evaluation tasks. However, current LLM-based techniques do not yet match the performance of human evaluators. We hypothesize that automatic evaluation can be improved by collecting a targeted UI feedback dataset and then using this dataset to enhance the performance of general-purpose LLMs. We present a targeted dataset of 3,059 design critiques and quality ratings for 983 mobile UIs, collected from seven designers, each with at least a year of professional design experience. We carried out an in-depth analysis to characterize the dataset's features. We then applied this dataset to achieve a 55\% performance gain in LLM-generated UI feedback via various few-shot and visual prompting techniques. We also discuss future applications of this dataset, including training a reward model for generative UI techniques, and fine-tuning a tool-agnostic multi-modal LLM that automates UI evaluation.



### EyeFormer: Predicting Personalized Scanpaths with Transformer-Guided Reinforcement Learning
Authors: Yue Jiang, Zixin Guo, Hamed Rezazadegan Tavakoli, Luis Leiva, Antti Oulasvirta

[Link](https://programs.sigchi.org/uist/2024/program/content/170925)

Abstract: From a visual-perception perspective, modern graphical user interfaces (GUIs) comprise a complex graphics-rich two-dimensional visuospatial arrangement of text, images, and interactive objects such as buttons and menus. While existing models can accurately predict regions and objects that are likely to attract attention ``on average'', no scanpath model has been capable of predicting scanpaths for an individual. To close this gap, we introduce EyeFormer, which utilizes a Transformer architecture as a policy network to guide a deep reinforcement learning algorithm that predicts gaze locations. Our model offers the unique capability of producing personalized predictions when given a few user scanpath samples. It can predict full scanpath information, including fixation positions and durations, across individuals and various stimulus types. Additionally, we demonstrate applications in GUI layout optimization driven by our model. 



### GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning
Authors: Minh Duc Vu, Han Wang, Jieshan Chen, Zhuang Li, Shengdong Zhao, Zhenchang Xing, Chunyang Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170994)

Abstract: Virtual assistants have the potential to play an important role in helping users achieve different tasks. However, these systems face challenges in their real-world usability, characterized by inefficiency and struggles in grasping user intentions. Leveraging recent advances in Large Language Models (LLMs), we introduce GPTVoiceTasker, a virtual assistant poised to enhance user experiences and task efficiency on mobile devices. GPTVoiceTasker excels at intelligently deciphering user commands and executing relevant device interactions to streamline task completion. For unprecedented tasks, GPTVoiceTasker utilises the contextual information and on-screen content to continuously explore and execute the tasks. In addition, the system continually learns from historical user commands to automate subsequent task invocations, further enhancing execution efficiency. From our experiments, GPTVoiceTasker achieved 84.5% accuracy in parsing human commands into executable actions and 85.7% accuracy in automating multi-step tasks. In our user study, GPTVoiceTasker boosted task efficiency in real-world scenarios by 34.85%, accompanied by positive participant feedback. We made GPTVoiceTasker open-source, inviting further research into LLMs utilization for diverse tasks through prompt engineering and leveraging user usage data to improve efficiency.



### VisionTasker: Mobile Task Automation Using Vision Based UI Understanding and LLM Task Planning
Authors: Yunpeng Song, Yiheng Bian, Yongtao Tang, Guiyu Ma, Zhongmin Cai

[Link](https://programs.sigchi.org/uist/2024/program/content/170816)

Abstract: Mobile task automation is an emerging field that leverages AI to streamline and optimize the execution of routine tasks on mobile devices, thereby enhancing efficiency and productivity. Traditional methods, such as Programming By Demonstration (PBD), are limited due to their dependence on predefined tasks and susceptibility to app updates. Recent advancements have utilized the view hierarchy to collect UI information and employed Large Language Models (LLM) to enhance task automation. However, view hierarchies have accessibility issues and face potential problems like missing object descriptions or misaligned structures. This paper introduces VisionTasker, a two-stage framework combining vision-based UI understanding and LLM task planning, for mobile task automation in a step-by-step manner. VisionTasker firstly converts a UI screenshot into natural language interpretations using a vision-based UI understanding approach, eliminating the need for view hierarchies. Secondly, it adopts a step-by-step task planning method, presenting one interface at a time to the LLM. The LLM then identifies relevant elements within the interface and determines the next action, enhancing accuracy and practicality. Extensive experiments show that VisionTasker outperforms previous methods, providing effective UI representations across four datasets. Additionally, in automating 147 real-world tasks on an Android smartphone, VisionTasker demonstrates advantages over humans in tasks where humans show unfamiliarity and shows significant improvements when integrated with the PBD mechanism. VisionTasker is open-source and available at https://github.com/AkimotoAyako/VisionTasker.




## Break Q&A: Poses as Input
### SolePoser: Real-Time 3D Human Pose Estimation using Insole Pressure Sensors
Authors: Erwin Wu, Rawal Khirodkar, Hideki Koike, Kris Kitani

[Link](https://programs.sigchi.org/uist/2024/program/content/170905)

Abstract: We propose SolePoser, a real-time 3D pose estimation system that leverages only a single pair of insole sensors. Unlike conventional methods relying on fixed cameras or bulky wearable sensors, our approach offers minimal and natural setup requirements. The proposed system utilizes pressure and IMU sensors embedded in insoles to capture the body weight's pressure distribution at the feet and its 6 DoF acceleration. This information is used to estimate the 3D full-body joint position by a two-stream transformer network. A novel double-cycle consistency loss and a cross-attention module are further introduced to learn the relationship between 3D foot positions and their pressure distributions.
We also introduced two different datasets of sports and daily exercises, offering 908k frames across eight different activities. Our experiments show that our method's performance is on par with top-performing approaches, which utilize more IMUs and even outperform third-person-view camera-based methods in certain scenarios. 



### Gait Gestures: Examining Stride and Foot Strike Variation as an Input Method While Walking
Authors: Ching-Yi Tsai, Ryan Yen, Daekun Kim, Daniel Vogel

[Link](https://programs.sigchi.org/uist/2024/program/content/170926)

Abstract: Walking is a cyclic pattern of alternating footstep strikes, with each pair of steps forming a stride, and a series of strides forming a gait.  We conduct a systematic examination of different kinds of intentional variations from a normal gait that could be used as input actions without interrupting overall walking progress. A design space of 22 candidate Gait Gestures is generated by adapting previous standing foot input actions and identifying new actions possible in a walking context.  A formative study (n=25) examines movement easiness, social acceptability, and walking compatibility with foot movement logging to calculate temporal and spatial characteristics. Using a categorization of these results, 7 gestures are selected for a wizard-of-oz prototype demonstrating an AR interface controlled by Gait Gestures for ordering food and audio playback while walking. As a technical proof-of-concept, a gait gesture recognizer is developed and tested using the formative study data.



### EgoTouch: On-Body Touch Input Using AR/VR Headset Cameras
Authors: Vimal Mollyn, Chris Harrison

[Link](https://programs.sigchi.org/uist/2024/program/content/170875)

Abstract: In augmented and virtual reality (AR/VR) experiences, a user’s arms and hands can provide a convenient and tactile surface for touch input. Prior work has shown on-body input to have significant speed, accuracy, and ergonomic benefits over in-air interfaces, which are common today. In this work, we demonstrate high accuracy, bare hands (i.e., no special instrumentation of the user) skin input using just an RGB camera, like those already integrated into all modern XR headsets. Our results show this approach can be accurate, and robust across diverse lighting conditions, skin tones, and body motion (e.g., input while walking). Finally, our pipeline also provides rich input metadata including touch force, finger identification, angle of attack, and rotation. We believe these are the requisite technical ingredients to more fully unlock on-skin interfaces that have been well motivated in the HCI literature but have lacked robust and practical methods.



### MobilePoser: Real-Time Full-Body Pose Estimation and 3D Human Translation from IMUs in Mobile Consumer Devices
Authors: Vasco Xu, Chenfeng Gao, Henry Hoffman, Karan Ahuja

[Link](https://programs.sigchi.org/uist/2024/program/content/170732)

Abstract: There has been a continued trend towards minimizing instrumentation for full-body motion capture, going from specialized rooms and equipment, to arrays of worn sensors and recently sparse inertial pose capture methods. However, as these techniques migrate towards lower-fidelity IMUs on ubiquitous commodity devices, like phones, watches, and earbuds, challenges arise including compromised online performance, temporal consistency, and loss of global translation due to sensor noise and drift. Addressing these challenges, we introduce MobilePoser, a real-time system for full-body pose and global translation estimation using any available subset of IMUs already present in these consumer devices. MobilePoser employs a multi-stage deep neural network for kinematic pose estimation followed by a physics-based motion optimizer, achieving state-of-the-art accuracy while remaining lightweight. We conclude with a series of demonstrative applications to illustrate the unique potential of MobilePoser across a variety of fields, such as health and wellness, gaming, and indoor navigation to name a few.  



### Touchscreen-based Hand Tracking for Remote Whiteboard Interaction
Authors: Xinshuang Liu, Yizhong Zhang, Xin Tong

[Link](https://programs.sigchi.org/uist/2024/program/content/170956)

Abstract: In whiteboard-based remote communication, the seamless integration of drawn content and hand-screen interactions is essential for an immersive user experience. Previous methods either require bulky device setups for capturing hand gestures or fail to accurately track the hand poses from capacitive images. In this paper, we present a real-time method for precise tracking 3D poses of both hands from capacitive video frames. To this end, we develop a deep neural network to identify hands and infer hand joint positions from capacitive frames, and then recover 3D hand poses from the hand-joint positions via a constrained inverse kinematic solver. Additionally, we design a device setup for capturing high-quality hand-screen interaction data and obtained a more accurate synchronized capacitive video and hand pose dataset. Our method improves the accuracy and stability of 3D hand tracking for capacitive frames while maintaining a compact device setup for remote communication. We validate our scheme design and its superior performance on 3D hand pose tracking and demonstrate the effectiveness of our method in whiteboard-based remote communication. 



### SeamPose: Repurposing Seams as Capacitive Sensors in a Shirt for Upper-Body Pose Tracking
Authors: Tianhong Yu, Mary Zhang, Peter He, Chi-Jung Lee, Cassidy Cheesman, Saif Mahmud, Ruidong Zhang, Francois Guimbretiere, Cheng Zhang

[Link](https://programs.sigchi.org/uist/2024/program/content/170739)

Abstract: Seams are areas of overlapping fabric formed by stitching two or more pieces of fabric together in the cut-and-sew apparel manufacturing process. In SeamPose, we repurposed seams as capacitive sensors in a shirt for continuous upper-body pose estimation. Compared to previous all-textile motion-capturing garments that place the electrodes on the clothing surface, our solution leverages existing seams inside of a shirt by machine-sewing insulated conductive threads over the seams. The unique invisibilities and placements of the seams afford the sensing shirt to look and wear similarly as a conventional shirt while providing exciting pose-tracking capabilities. To validate this approach, we implemented a proof-of-concept untethered shirt with 8 capacitive sensing seams. With a 12-participant user study, our customized deep-learning pipeline accurately estimates the relative (to the pelvis) upper-body 3D joint positions with a mean per joint position error (MPJPE) of 6.0 cm. SeamPose represents a step towards unobtrusive integration of smart clothing for everyday pose estimation.




## Break Q&A: A11y
### ProgramAlly: Creating Custom Visual Access Programs via Multi-Modal End-User Programming
Authors: Jaylin Herskovitz, Andi Xu, Rahaf Alharbi, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170960)

Abstract: Existing visual assistive technologies are built for simple and common use cases, and have few avenues for blind people to customize their functionalities. Drawing from prior work on DIY assistive technology, this paper investigates end-user programming as a means for users to create and customize visual access programs to meet their unique needs. We introduce ProgramAlly, a system for creating custom filters for visual information, e.g., 'find NUMBER on BUS', leveraging three end-user programming approaches: block programming, natural language, and programming by example. To implement ProgramAlly, we designed a representation of visual filtering tasks based on scenarios encountered by blind people, and integrated a set of on-device and cloud models for generating and running these programs. In user studies with 12 blind adults, we found that participants preferred different programming modalities depending on the task, and envisioned using visual access programs to address unique accessibility challenges that are otherwise difficult with existing applications. Through ProgramAlly, we present an exploration of how blind end-users can create visual access programs to customize and control their experiences.



### Accessible Gesture Typing on Smartphones for People with Low Vision
Authors: Dan Zhang, Zhi Li, Vikas Ashok, William H Seiple, IV Ramakrishnan, Xiaojun Bi

[Link](https://programs.sigchi.org/uist/2024/program/content/170887)

Abstract: While gesture typing is widely adopted on touchscreen keyboards, its support for low vision users is limited.  We have designed and implemented two keyboard prototypes, layout-magnified and key-magnified keyboards, to enable gesture typing for people with low vision. Both keyboards facilitate uninterrupted access to all keys while the screen magnifier is active, allowing people with low vision to input text with one continuous stroke. Furthermore, we have created a kinematics-based decoding algorithm to accommodate the typing behavior of people with low vision. This algorithm can decode the gesture input even if the gesture trace deviates from a pre-defined word template, and the starting position of the gesture is far from the starting letter of the target word. Our user study showed that the key-magnified keyboard achieved 5.28 words per minute, 27.5% faster than a conventional gesture typing keyboard with voice feedback.



### AccessTeleopKit: A Toolkit for Creating Accessible Web-Based Interfaces for Tele-Operating an Assistive Robot
Authors: Vinitha Ranganeni, Varad Dhat, Noah Ponto, Maya Cakmak

[Link](https://programs.sigchi.org/uist/2024/program/content/170825)

Abstract: Mobile manipulator robots, which can move around and physically interact with their environments, can empower people with motor limitations to independently carry out many activities of daily living. While many interfaces have been developed for tele-operating complex robots, most of them are not accessible to people with severe motor limitations. Further, most interfaces are rigid with limited configurations and are not readily available to download and use. To address these barriers, we developed AccessTeleopKit: an open-source toolkit for creating custom and accessible robot tele-operation interfaces based on cursor-and-click input for the Stretch 3 mobile-manipulator. With AccessTeleopKit users can add, remove, and rearrange components such as buttons and camera views, and select between a variety of control modes. We describe the participatory and iterative design process that led to the current implementation of AccessTeleopKit, involving three long-term deployments of the robot in the home of a quadriplegic user. We demonstrate how AccessTeleopKit allowed the user to create different interfaces for different tasks and the diversity of tasks it allowed the user to carry out. We also present two studies involving six additional users with severe motor limitations, demonstrating the power of AccessTeleopKit in creating custom interfaces for different user needs and preferences.



### Memory Reviver: Supporting Photo-Collection Reminiscence for People with Visual Impairment via a Proactive Chatbot
Authors: Shuchang Xu, Chang Chen, Zichen LIU, Xiaofu Jin, Linping Yuan, Yukang Yan, Huamin Qu

[Link](https://programs.sigchi.org/uist/2024/program/content/170852)

Abstract: Reminiscing with photo collections offers significant psychological benefits but poses challenges for people with visual impairment (PVI). Their current reliance on sighted help restricts the flexibility of this activity. In response, we explored using a chatbot in a preliminary study. We identified two primary challenges that hinder effective reminiscence with a chatbot: the scattering of information and a lack of proactive guidance. To address these limitations, we present Memory Reviver, a proactive chatbot that helps PVI reminisce with a photo collection through natural language communication. Memory Reviver incorporates two novel features: (1) a Memory Tree, which uses a hierarchical structure to organize the information in a photo collection; and (2) a Proactive Strategy, which actively delivers information to users at proper conversation rounds. Evaluation with twelve PVI demonstrated that Memory Reviver effectively facilitated engaging reminiscence, enhanced understanding of photo collections, and delivered natural conversational experiences. Based on our findings, we distill implications for supporting photo reminiscence and designing chatbots for PVI.



### VizAbility: Enhancing Chart Accessibility with LLM-based Conversational Interaction
Authors: Joshua Gorniak, Yoon Kim, Donglai Wei, Nam Wook Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/171009)

Abstract: Traditional accessibility methods like alternative text and data tables typically underrepresent data visualization's full potential. Keyboard-based chart navigation has emerged as a potential solution, yet efficient data exploration remains challenging. We present VizAbility, a novel system that enriches chart content navigation with conversational interaction, enabling users to use natural language for querying visual data trends. VizAbility adapts to the user's navigation context for improved response accuracy and facilitates verbal command-based chart navigation. Furthermore, it can address queries for contextual information, designed to address the needs of visually impaired users. We designed a large language model (LLM)-based pipeline to address these user queries, leveraging chart data & encoding, user context, and external web knowledge. We conducted both qualitative and quantitative studies to evaluate VizAbility's multimodal approach. We discuss further opportunities based on the results, including improved benchmark testing, incorporation of vision models, and integration with visualization workflows.



### Computational Trichromacy Reconstruction: Empowering the Color-Vision Deficient to Recognize Colors Using Augmented Reality
Authors: Yuhao Zhu, Ethan Chen, Colin Hascup, Yukang Yan, Gaurav Sharma

[Link](https://programs.sigchi.org/uist/2024/program/content/170991)

Abstract: We propose an assistive technology that helps individuals with Color Vision Deficiencies (CVD) to recognize/name colors.
A dichromat's color perception is a reduced two-dimensional (2D) subset of a normal
trichromat's three dimensional color (3D) perception, leading to confusion when visual stimuli that appear identical to the dichromat are referred to by different color names.
Using our proposed system, CVD individuals can interactively induce distinct perceptual changes to originally confusing colors via a computational color space transformation.
By combining their original 2D precepts for colors with the discriminative changes, a three dimensional color space is reconstructed, where the dichromat can learn to resolve color name confusions and accurately recognize colors.
Our system is implemented as an Augmented Reality (AR) interface on smartphones, where users interactively control the rotation through swipe gestures and observe the induced color shifts in the camera view or in a displayed image. Through psychophysical experiments and a longitudinal user study, we demonstrate that such rotational color shifts have discriminative power (initially confusing colors become distinct under rotation) and exhibit structured perceptual shifts dichromats can learn with modest training. The AR App is also evaluated in two real-world scenarios (building with lego blocks and interpreting artistic works); users all report positive experience in using the App to recognize object colors that they otherwise could not.




## Break Q&A: Sustainable Interfaces
### Degrade to Function: Towards Eco-friendly Morphing Devices that Function Through Programmed Sequential Degradation
Authors: Qiuyu Lu, Semina Yi, Mengtian Gan, Jihong Huang, Xiao Zhang, Yue Yang, Chenyi Shen, Lining Yao

[Link](https://programs.sigchi.org/uist/2024/program/content/170959)

Abstract: While it seems counterintuitive to think of degradation within an operating device as beneficial, one may argue that when rationally designed, the controlled breakdown of materials—physical, chemical, or biological—can be harnessed for specific functions. To apply this principle to the design of morphing devices, we introduce the concept of "Degrade to Function" (DtF). This concept aims to create eco-friendly and self-contained morphing devices that operate through a sequence of environmentally-triggered degradations. We explore its design considerations and implementation techniques by identifying environmental conditions and degradation types that can be exploited, evaluating potential materials capable of controlled degradation, suggesting designs for structures that can leverage degradation to achieve various transformations and functions, and developing sequential control approaches that integrate degradation triggers. To demonstrate the viability and versatility of this design strategy, we showcase several application examples across a range of environmental conditions.



### WasteBanned: Supporting Zero Waste Fashion Design Through Linked Edits
Authors: Ruowang Zhang, Stefanie Mueller, Gilbert Bernstein, Adriana Schulz, Mackenzie Leake

[Link](https://programs.sigchi.org/uist/2024/program/content/170976)

Abstract: The commonly used cut-and-sew garment construction process, in which 2D fabric panels are cut from sheets of fabric and assembled into 3D garments, contributes to widespread textile waste in the fashion industry. There is often a significant divide between the design of the garment and the layout of the panels. One opportunity for bridging this gap is the emerging study and practice of zero waste fashion design, which involves creating clothing designs with maximum layout efficiency. Enforcing the strict constraints of zero waste sewing is challenging, as edits to one region of the garment necessarily affect neighboring panels. Based on our formative work to understand this emerging area within fashion design, we present WasteBanned, a tool that combines CAM and CAD to help users prioritize efficient material usage, work within these zero waste constraints, and edit existing zero waste garment patterns. Our user evaluation indicates that our tool helps fashion designers edit zero waste patterns to fit different bodies and add stylistic variation, while creating highly efficient fabric layouts.



### HoloChemie - Sustainable Fabrication of Soft Biochemical Holographic Devices for Ubiquitous Sensing
Authors: Sutirtha Roy, Moshfiq-Us-Saleheen Chowdhury, Jurjaan Noim, Richa Pandey, Aditya Shekhar Nittala

[Link](https://programs.sigchi.org/uist/2024/program/content/170931)

Abstract: Sustainable fabrication approaches and biomaterials are increasingly being used in HCI to fabricate interactive devices. However, the majority of the work has focused on integrating electronics. This paper takes a sustainable approach to exploring the fabrication of biochemical sensing devices. Firstly, we contribute a set of biochemical formulations for biological and environmental sensing with bio-sourced and environment-friendly substrate materials. Our formulations are based on a combination of enzymes derived from bacteria and fungi, plant extracts and commercially available chemicals to sense both liquid and gaseous analytes: glucose, lactic acid, pH levels and carbon dioxide. Our novel holographic sensing scheme allows for detecting the presence of analytes and enables quantitative estimation of the analyte levels. We present a set of application scenarios that demonstrate the versatility of our approach and discuss the sustainability aspects, its limitations, and the implications for bio-chemical systems in HCI.




## Break Q&A: FABulous
### Facilitating the Parametric Definition of Geometric Properties in Programming-Based CAD
Authors: J Gonzalez Avila, Thomas Pietrzak, Audrey Girouard, Géry Casiez

[Link](https://programs.sigchi.org/uist/2024/program/content/170736)

Abstract: Parametric Computer-aided design (CAD) enables the creation of reusable models by integrating variables into geometric properties, facilitating customization without a complete redesign. However, creating parametric designs in programming-based CAD presents significant challenges. Users define models in a code editor using a programming language, with the application generating a visual representation in a viewport. This process involves complex programming and arithmetic expressions to describe geometric properties, linking various object properties to create parametric designs. Unfortunately, these applications lack assistance, making the process unnecessarily demanding. We propose a solution that allows users to retrieve parametric expressions from the visual representation for reuse in the code, streamlining the design process. We demonstrated this concept through a proof-of-concept implemented in the programming-based CAD application, OpenSCAD, and conducted an experiment with 11 users. Our findings suggest that this solution could significantly reduce design errors, improve interactivity and engagement in the design process, and lower the entry barrier for newcomers by reducing the mathematical skills typically required in programming-based CAD applications



### Rhapso: Automatically Embedding Fiber Materials into 3D Prints for Enhanced Interactivity
Authors: Daniel Ashbrook, Wei-Ju Lin, Nicholas Bentley, Diana Soponar, Zeyu Yan, Valkyrie Savage, Lung-Pan Cheng, Huaishu Peng, Hyunyoung Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170936)

Abstract:    We introduce Rhapso, a 3D printing system designed to embed a diverse range of continuous fiber materials within 3D objects during the printing process. This approach enables integrating properties like tensile strength, force storage and transmission, or aesthetic and tactile characteristics, directly into low-cost thermoplastic 3D prints. These functional objects can have intricate actuation, self-assembly, and sensing capabilities with little to no manual intervention. To achieve this, we modify a low-cost Fused Filament Fabrication (FFF) 3D printer, adding a stepper motor-controlled fiber spool mechanism on a gear ring above the print bed. In addition to hardware, we provide parsing software for precise fiber placement, which generates Gcode for printer operation. To illustrate the versatility of our system, we present applications that showcase its extensive design potential. Additionally, we offer comprehensive documentation and open designs, empowering others to replicate our system and explore its possibilities.




### Speed-Modulated Ironing: High-Resolution Shade and Texture Gradients in Single-Material 3D Printing
Authors: Mehmet Ozdemir, Marwa AlAlawi, Mustafa Doga Dogan, Jose Martinez Castro, Stefanie Mueller, Zjenja Doubrovski

[Link](https://programs.sigchi.org/uist/2024/program/content/170731)

Abstract: We present Speed-Modulated Ironing, a new fabrication method for programming visual and tactile properties in single-material 3D printing. We use one nozzle to 3D print and a second nozzle to reheat printed areas at varying speeds, controlling the material's temperature-response. The rapid adjustments of speed allow for fine-grained reheating, enabling high-resolution color and texture variations. We implemented our method in a tool that allows users to assign desired properties to 3D models and creates corresponding 3D printing instructions. We demonstrate our method with three temperature-responsive materials: a foaming filament, a filament with wood fibers, and a filament with cork particles.  These filaments respond to temperature by changing color, roughness, transparency, and gloss. Our technical evaluation reveals the capabilities of our method in achieving sufficient resolution and color shade range that allows surface details such as small text, photos, and QR codes on 3D-printed objects. Finally, we provide application examples demonstrating the new design capabilities enabled by Speed-Modulated Ironing.



### TRAvel Slicer: Continuous Extrusion Toolpaths for 3D Printing
Authors: Jaime Gould, Camila Friedman-Gerlicz, Leah Buechley

[Link](https://programs.sigchi.org/uist/2024/program/content/170996)

Abstract: In this paper we present Travel Reduction Algorithm (TRAvel) Slicer, which minimizes travel movements in 3D printing. Conventional slicing software generates toolpaths with many travel movements--movements without material extrusion. Some 3D printers are incapable of starting and stopping extrusion and it is difficult to impossible to control the extrusion of many materials. This makes toolpaths with travel movements unsuitable for a wide range of printers and materials. 

We developed the open-source TRAvel Slicer to enable the printing of complex 3D models on a wider range of printers and in a wider range of materials than is currently possible. TRAvel Slicer minimizes two different kinds of travel movements--what we term Inner- and Outer-Model travel. We minimize Inner-Model travel (travel within the 3D model) by generating space-filling Fermat spirals for each contiguous planar region of the model. We minimize Outer-Model travel (travels outside of the 3D model) by ordering the printing of different branches of the model, thus limiting transitions between branches. We present our algorithm and software and then demonstrate how: 1) TRAvel Slicer makes it possible to generate high-quality prints from a metal-clay material, CeraMetal, that is functionally unprintable using an off-the-shelf slicer. 2) TRAvel Slicer dramatically increases the printing efficiency of traditional plastic 3D printing compared to an off-the-shelf slicer.



### Understanding and Supporting Debugging Workflows in CAD
Authors: Felix Hähnlein, Gilbert Bernstein, Adriana Schulz

[Link](https://programs.sigchi.org/uist/2024/program/content/170944)

Abstract: One of the core promises of parametric Computer-Aided Design (CAD) is that users can easily edit their model at any point in time.
However, due to the ambiguity of changing references to intermediate, updated geometry, parametric edits can lead to reference errors which are difficult to fix in practice.
We claim that debugging reference errors remains challenging because CAD systems do not provide users with tools to understand where the error happened and how to fix it.
To address these challenges, we prototype a graphical debugging tool, DeCAD, which helps comparing CAD model states both across operations and across edits.
In a qualitative lab study, we use DeCAD as a probe to understand specific challenges that users face and what workflows they employ to overcome them.
We conclude with design implications for future debugging tool developers. 





## Break Q&A: Programming UI
### NotePlayer: Engaging Jupyter Notebooks for Dynamic Presentation of Analytical Processes
Authors: Yang Ouyang, Leixian Shen, Yun Wang, Quan Li

[Link](https://programs.sigchi.org/uist/2024/program/content/170819)

Abstract: Diverse presentation formats play a pivotal role in effectively conveying code and analytical processes during data analysis. One increasingly popular format is tutorial videos, particularly those based on Jupyter notebooks, which offer an intuitive interpretation of code and vivid explanations of analytical procedures. However, creating such videos requires a diverse skill set and significant manual effort, posing a barrier for many analysts. To bridge this gap, we introduce an innovative tool called NotePlayer, which connects notebook cells to video segments and incorporates a computational engine with language models to streamline video creation and editing. Our aim is to make the process more accessible and efficient for analysts. To inform the design of NotePlayer, we conducted a formative study and performed content analysis on a corpus of 38 Jupyter tutorial videos. This helped us identify key patterns and challenges encountered in existing tutorial videos, guiding the development of NotePlayer. Through a combination of a usage scenario and a user study, we validated the effectiveness of NotePlayer. The results show that the tool streamlines the video creation and facilitates the communication process for data analysts.



### Tyche: Making Sense of Property-Based Testing Effectiveness
Authors: Harrison Goldstein, Jeffrey Tao, Zac Hatfield-Dodds, Benjamin Pierce, Andrew Head

[Link](https://programs.sigchi.org/uist/2024/program/content/170922)

Abstract: Software developers increasingly rely on automated methods to assess the
correctness of their code. One such method is property-based testing
(PBT), wherein a test harness generates hundreds or thousands of inputs
and checks the outputs of the program on those inputs using parametric
properties. Though powerful, PBT induces a sizable gulf of evaluation:
developers need to put in nontrivial effort to understand how well the
different test inputs exercise the software under test. To bridge this
gulf, we propose Tyche, a user interface that supports sensemaking
around the effectiveness of property-based tests. Guided by a formative
design exploration, our design of Tyche supports developers with
interactive, configurable views of test behavior with tight integrations
into modern developer testing workflow. These views help developers
explore global testing behavior and individual test inputs alike. To
accelerate the development of powerful, interactive PBT tools, we define
a standard for PBT test reporting and integrate it with a widely used
PBT library. A self-guided online usability study revealed that Tyche's
visualizations help developers to more accurately assess software
testing effectiveness.




### CoLadder: Manipulating Code Generation via Multi-Level Blocks
Authors: Ryan Yen, Jiawen Zhu, Sangho Suh, Haijun Xia, Jian Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/171012)

Abstract: This paper adopted an iterative design process to gain insights into programmers' strategies when using LLMs for programming. We proposed CoLadder, a novel system that supports programmers by facilitating hierarchical task decomposition, direct code segment manipulation, and result evaluation during prompt authoring. A user study with 12 experienced programmers showed that CoLadder is effective in helping programmers externalize their problem-solving intentions flexibly, improving their ability to evaluate and modify code across various abstraction levels, from their task's goal to final code implementation.



### SQLucid: Grounding Natural Language Database Queries with Interactive Explanations
Authors: Yuan Tian, Jonathan Kummerfeld, Toby Li, Tianyi Zhang

[Link](https://programs.sigchi.org/uist/2024/program/content/170951)

Abstract: Though recent advances in machine learning have led to significant improvements in natural language interfaces for databases, the accuracy and reliability of these systems remain limited, especially in high-stakes domains. This paper introduces SQLucid, a novel user interface that bridges the gap between non-expert users and complex database querying processes. SQLucid addresses existing limitations by integrating visual correspondence, intermediate query results, and editable step-by-step SQL explanations in natural language to facilitate user understanding and engagement. This unique blend of features empowers users to understand and refine SQL queries easily and precisely. Two user studies and one quantitative experiment were conducted to validate SQLucid’s effectiveness, showing significant improvement in task completion accuracy and user confidence compared to existing interfaces. Our code is available at https://github.com/magic-YuanTian/SQLucid.




## Break Q&A: AI & Automation
### Memolet: Reifying the Reuse of User-AI Conversational Memories
Authors: Ryan Yen, Jian Zhao

[Link](https://programs.sigchi.org/uist/2024/program/content/170751)

Abstract: As users engage more frequently with AI conversational agents, conversations may exceed their memory capacity, leading to failures in correctly leveraging certain memories for tailored responses. However, in finding past memories that can be reused or referenced, users need to retrieve relevant information in various conversations and articulate to the AI their intention to reuse these memories. To support this process, we introduce Memolet, an interactive object that reifies memory reuse. Users can directly manipulate Memolet to specify which memories to reuse and how to use them. We developed a system demonstrating Memolet's interaction across various memory reuse stages, including memory extraction, organization, prompt articulation, and generation refinement. We examine the system's usefulness with an N=12 within-subject study and provide design implications for future systems that support user-AI conversational memory reusing.



### VIME: Visual Interactive Model Explorer for Identifying Capabilities and Limitations of Machine Learning Models for Sequential Decision-Making
Authors: Anindya Das Antar, Somayeh Molaei, Yan-Ying Chen, Matthew Lee, Nikola Banovic

[Link](https://programs.sigchi.org/uist/2024/program/content/170861)

Abstract: Ensuring that Machine Learning (ML) models make correct and meaningful inferences is necessary for the broader adoption of such models into high-stakes decision-making scenarios. Thus, ML model engineers increasingly use eXplainable AI (XAI) tools to investigate the capabilities and limitations of their ML models before deployment. However, explaining sequential ML models, which make a series of decisions at each timestep, remains challenging. We present Visual Interactive Model Explorer (VIME), an XAI toolbox that enables ML model engineers to explain decisions of sequential models in different ``what-if'' scenarios. Our evaluation with 14 ML experts, who investigated two existing sequential ML models using VIME and a baseline XAI toolbox to explore ``what-if'' scenarios, showed that VIME made it easier to identify and explain instances when the models made wrong decisions compared to the baseline. Our work informs the design of future interactive XAI mechanisms for evaluating sequential ML-based decision support systems.



### SERENUS: Alleviating Low-Battery Anxiety Through Real-time, Accurate, and User-Friendly Energy Consumption Prediction of Mobile Applications
Authors: Sera Lee, Dae R. Jeong, Junyoung Choi, Jaeheon Kwak, Seoyun Son, Jean Song, Insik Shin

[Link](https://programs.sigchi.org/uist/2024/program/content/170937)

Abstract: Low-battery anxiety has emerged as a result of growing dependence on mobile devices, where the anxiety arises when the battery level runs low. While battery life can be extended through power-efficient hardware and software optimization techniques, low-battery anxiety will remain a phenomenon as long as mobile devices rely on batteries. In this paper, we investigate how an accurate real-time energy consumption prediction at the application-level can improve the user experience in low-battery situations. We present Serenus, a mobile system framework specifically tailored to predict the energy consumption of each mobile application and present the prediction in a user-friendly manner. We conducted user studies using Serenus to verify that highly accurate energy consumption predictions can effectively alleviate low-battery anxiety by assisting users in planning their application usage based on the remaining battery life. We summarize requirements to mitigate users’ anxiety, guiding the design of future mobile system frameworks.




## Break Q&A: AI as Copilot
### DiscipLink: Unfolding Interdisciplinary Information Seeking Process via Human-AI Co-Exploration
Authors: Chengbo Zheng, Yuanhao Zhang, Zeyu Huang, Chuhan Shi, Minrui Xu, Xiaojuan Ma

[Link](https://programs.sigchi.org/uist/2024/program/content/170741)

Abstract: Interdisciplinary studies often require researchers to explore literature in diverse branches of knowledge. Yet, navigating through the highly scattered knowledge from unfamiliar disciplines poses a significant challenge. In this paper, we introduce DiscipLink, a novel interactive system that facilitates collaboration between researchers and large language models (LLMs) in interdisciplinary information seeking (IIS). Based on users' topic of interest, DiscipLink initiates exploratory questions from the perspectives of possible relevant fields of study, and users can further tailor these questions. DiscipLink then supports users in searching and screening papers under selected questions by automatically expanding queries with disciplinary-specific terminologies, extracting themes from retrieved papers, and highlighting the connections between papers and questions. Our evaluation, comprising a within-subject comparative experiment and an open-ended exploratory study, reveals that DiscipLink can effectively support researchers in breaking down disciplinary boundaries and integrating scattered knowledge in diverse fields. The findings underscore the potential of LLM-powered tools in fostering information-seeking practices and bolstering interdisciplinary research.



### Improving Steering and Verification in AI-Assisted Data Analysis with Interactive Task Decomposition
Authors: Majeed Kazemitabaar, Jack Williams, Ian Drosos, Tovi Grossman, Austin Henley, Carina Negreanu, Advait Sarkar

[Link](https://programs.sigchi.org/uist/2024/program/content/170918)

Abstract: LLM-powered tools like ChatGPT Data Analysis, have the potential to help users tackle the challenging task of data analysis programming, which requires expertise in data processing, programming, and statistics. However, our formative study (n=15) uncovered serious challenges in verifying AI-generated results and steering the AI (i.e., guiding the AI system to produce the desired output). We developed two contrasting approaches to address these challenges. The first (Stepwise) decomposes the problem into step-by-step subgoals with pairs of editable assumptions and code until task completion, while the second (Phasewise) decomposes the entire problem into three editable, logical phases: structured input/output assumptions, execution plan, and code. A controlled, within-subjects experiment (n=18) compared these systems against a conversational baseline. Users reported significantly greater control with the Stepwise and Phasewise systems, and found intervention, correction, and verification easier, compared to the baseline. The results suggest design guidelines and trade-offs for AI-assisted data analysis tools.




### VizGroup: An AI-assisted Event-driven System for Collaborative Programming Learning Analytics
Authors: Xiaohang Tang, Sam Wong, Kevin Pu, Xi Chen, Yalong Yang, Yan Chen

[Link](https://programs.sigchi.org/uist/2024/program/content/170725)

Abstract: Programming instructors often conduct collaborative learning activities, like Peer Instruction, to foster a deeper understanding in students and enhance their engagement with learning. These activities, however, may not always yield productive outcomes due to the diversity of student mental models and their ineffective collaboration. In this work, we introduce VizGroup, an AI-assisted system that enables programming instructors to easily oversee students' real-time collaborative learning behaviors during large programming courses. VizGroup leverages Large Language Models (LLMs) to recommend event specifications for instructors so that they can simultaneously track and receive alerts about key correlation patterns between various collaboration metrics and ongoing coding tasks. We evaluated VizGroup with 12 instructors in a comparison study using a dataset collected from a Peer Instruction activity that was conducted in a large programming lecture. 
The results showed that VizGroup helped instructors effectively overview, narrow down, and track nuances throughout students' behaviors.



### Who did it? How User Agency is influenced by Visual Properties of Generated Images
Authors: Johanna Didion, Krzysztof Wolski, Dennis Wittchen, David Coyle, Thomas Leimkühler, Paul Strohmeier

[Link](https://programs.sigchi.org/uist/2024/program/content/170827)

Abstract: The increasing proliferation of AI and GenAI requires new interfaces tailored to how their specific affordances and human requirements meet. As GenAI is capable of taking over tasks from users on an unprecedented scale, designing the experience of agency -- if and how users experience control over the process and responsibility over the outcome -- is crucial. As an initial step towards design guidelines for shaping agency, we present a study that explores how features of AI-generated images influence users' experience of agency. We use two measures; temporal binding to implicitly estimate pre-reflective agency and magnitude estimation to assess user judgments of agency. We observe that abstract images lead to more temporal binding than images with semantic meaning. In contrast, the closer an image aligns with what a user might expect, the higher the agency judgment. When comparing the experiment results with objective metrics of image differences, we find that temporal binding results correlate with semantic differences, while agency judgments are better explained by local differences between images. This work contributes towards a future where agency is considered an important design dimension for GenAI interfaces.



### FathomGPT: A Natural Language Interface for Interactively Exploring Ocean Science Data
Authors: Nabin Khanal, Chun Meng Yu, Jui-Cheng Chiu, Anav Chaudhary, Ziyue Zhang, Kakani Katija, Angus Forbes

[Link](https://programs.sigchi.org/uist/2024/program/content/171001)

Abstract: We introduce FathomGPT, an open source system for the interactive investigation of ocean science data via a natural language interface. FathomGPT was developed in close collaboration with marine scientists to enable researchers and ocean enthusiasts to explore and analyze the FathomNet image database. FathomGPT provides a custom information retrieval pipeline that leverages OpenAI’s large language models to enable: the creation of complex queries to retrieve images, taxonomic information, and scientific measurements; mapping common names and morphological features to scientific names; generating interactive charts on demand; and searching by image or specified patterns within an image. In designing FathomGPT, particular emphasis was placed on enhancing the user's experience by facilitating free-form exploration and optimizing response times. We present an architectural overview and implementation details of  FathomGPT, along with a series of ablation studies that demonstrate the effectiveness of our approach to name resolution, fine tuning, and prompt modification. Additionally, we present usage scenarios of interactive data exploration sessions and document feedback from ocean scientists and machine learning experts.



### VRCopilot: Authoring 3D Layouts with Generative AI Models in VR
Authors: Lei Zhang, Jin Pan, Jacob Gettig, Steve Oney, Anhong Guo

[Link](https://programs.sigchi.org/uist/2024/program/content/170933)

Abstract: Immersive authoring provides an intuitive medium for users to create 3D scenes via direct manipulation in Virtual Reality (VR). Recent advances in generative AI have enabled the automatic creation of realistic 3D layouts. However, it is unclear how capabilities of generative AI can be used in immersive authoring to support fluid interactions, user agency, and creativity. We introduce VRCopilot, a mixed-initiative system that integrates pre-trained generative AI models into immersive authoring to facilitate human-AI co-creation in VR. VRCopilot presents multimodal interactions to support rapid prototyping and iterations with AI, and intermediate representations such as wireframes to augment user controllability over the created content. Through a series of user studies, we evaluated the potential and challenges in manual, scaffolded, and automatic creation in immersive authoring. We found that scaffolded creation using wireframes enhanced the user agency compared to automatic creation. We also found that manual creation via multimodal specification offers the highest sense of creativity and agency.




## Break Q&A: Validation in AI/ML
### Natural Expression of a Machine Learning Model's Uncertainty Through Verbal and Non-Verbal Behavior of Intelligent Virtual Agents
Authors: Susanne Schmidt, Tim Rolff, Henrik Voigt, Micha Offe, Frank Steinicke

[Link](https://programs.sigchi.org/uist/2024/program/content/170826)

Abstract: Uncertainty cues are inherent in natural human interaction, as they signal to communication partners how much they can rely on conveyed information. Humans subconsciously provide such signals both verbally (e.g., through expressions such as "maybe" or "I think") and non-verbally (e.g., by diverting their gaze). In contrast, artificial intelligence (AI)-based services and machine learning (ML) models such as ChatGPT usually do not disclose the reliability of answers to their users.
In this paper, we explore the potential of combining ML models as powerful information sources with human means of expressing uncertainty to contextualize the information. We present a comprehensive pipeline that comprises (1) the human-centered collection of (non-)verbal uncertainty cues, (2) the transfer of cues to virtual agent videos, (3) the annotation of videos for perceived uncertainty, and (4) the subsequent training of a custom ML model that can generate uncertainty cues in virtual agent behavior. In a final step (5), the trained ML model is evaluated in terms of both fidelity and generalizability of the generated (non-)verbal uncertainty behavior.



### Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
Authors: Shreya Shankar, J.D. Zamfirescu-Pereira, Bjoern Hartmann, Aditya Parameswaran, Ian Arawjo

[Link](https://programs.sigchi.org/uist/2024/program/content/170954)

Abstract: Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs. Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation. We present a mixed-initiative approach to “validate the validators”— aligning LLM-generated evaluation functions (be it prompts or code) with human requirements. Our interface, EvalGen, provides automated assistance to users in generating evaluation criteria and implementing assertions. While generating candidate implementations (Python functions, LLM grader prompts), EvalGen asks humans to grade a subset of LLM outputs; this feedback is used to select implementations that better align with user grades. A qualitative study finds overall support for EvalGen but underscores the subjectivity and iterative nature of alignment. In particular, we identify a phenomenon we dub criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appear dependent on the specific LLM outputs observed (rather than independent and definable a priori), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs. We present our interface and implementation details, a comparison of our algorithm with a baseline approach, and implications for the design of future LLM evaluation assistants.



### LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation
Authors: Li Zhang, Shihe Wang, Xianqing Jia, Zhihan Zheng, Yunhe Yan, Longxi Gao, Yuanchun Li, Mengwei Xu

[Link](https://programs.sigchi.org/uist/2024/program/content/170831)

Abstract: The emergent large language/multimodal models facilitate the evolution of mobile agents, especially in mobile UI task automation. However, existing evaluation approaches, which rely on human validation or established datasets to compare agent-predicted actions with predefined action sequences, are unscalable and unfaithful. To overcome these limitations, this paper presents LlamaTouch, a testbed for on-device mobile UI task execution and faithful, scalable task evaluation. By observing that the task execution process only transfers UI states, LlamaTouch employs a novel evaluation approach that only assesses whether an agent traverses all manually annotated, essential application/system states. LlamaTouch comprises three key techniques: (1) On-device task execution that enables mobile agents to interact with realistic mobile environments for task execution. (2) Fine-grained UI component annotation that merges pixel-level screenshots and textual screen hierarchies to explicitly identify and precisely annotate essential UI components with a rich set of designed annotation primitives. (3) A multi-level application state matching algorithm that utilizes exact and fuzzy matching to accurately detect critical information in each screen, even with unpredictable UI layout/content dynamics. LlamaTouch currently incorporates four mobile agents and 496 tasks, encompassing both tasks in the widely-used datasets and our self-constructed ones to cover more diverse mobile applications. Evaluation results demonstrate LlamaTouch’s high faithfulness of evaluation in real-world mobile environments and its better scalability than human validation. LlamaTouch also enables easy task annotation and integration of new mobile agents. Code and dataset are publicly available at https://github.com/LlamaTouch/LlamaTouch.



### Clarify: Improving Model Robustness With Natural Language Corrections
Authors: Yoonho Lee, Michelle Lam, Helena Vasconcelos, Michael Bernstein, Chelsea Finn

[Link](https://programs.sigchi.org/uist/2024/program/content/170784)

Abstract: The standard way to teach models is by feeding them lots of data. However, this approach often teaches models incorrect ideas because they pick up on misleading signals in the data. To prevent such misconceptions, we must necessarily provide additional information beyond the training data.  Prior methods incorporate additional instance-level supervision, such as labels for misleading features or additional labels for debiased data.  However, such strategies require a large amount of labeler effort. We hypothesize that people are good at providing textual feedback at the concept level, a capability that existing teaching frameworks do not leverage. We propose Clarify, a novel interface and method for interactively correcting model misconceptions. Through Clarify, users need only provide a short text description of a model's consistent failure patterns. Then, in an entirely automated way, we use such descriptions to improve the training process. Clarify is the first end-to-end system for user model correction. Our user studies show that non-expert users can successfully describe model misconceptions via Clarify, leading to increased worst-case performance in two datasets. We additionally conduct a case study on a large-scale image dataset, ImageNet, using Clarify to find and rectify 31 novel hard subpopulations.



### "The Data Says Otherwise" – Towards Automated Fact-checking and Communication of Data Claims
Authors: Yu Fu, Shunan Guo, Jane Hoffswell, Victor S. Bursztyn, Ryan Rossi, John Stasko

[Link](https://programs.sigchi.org/uist/2024/program/content/170762)

Abstract: Fact-checking data claims requires data evidence retrieval and analysis, which can become tedious and intractable when done manually. This work presents Aletheia, an automated fact-checking prototype designed to facilitate data claims verification and enhance data evidence communication. For verification, we utilize a pre-trained LLM to parse the semantics for evidence retrieval. To effectively communicate the data evidence, we design representations in two forms: data tables and visualizations, tailored to various data fact types. Additionally, we design interactions that showcase a real-world application of these techniques. We evaluate the performance of two core NLP tasks with a curated dataset comprising 400 data claims and compare the two representation forms regarding viewers’ assessment time, confidence, and preference via a user study with 20 participants. The evaluation offers insights into the feasibility and bottlenecks of using LLMs for data fact-checking tasks, potential advantages and disadvantages of using visualizations over data tables, and design recommendations for presenting data evidence.




## Break Q&A: Bodily Signals
### Empower Real-World BCIs with NIRS-X: An Adaptive Learning Framework that Harnesses Unlabeled Brain Signals
Authors: Liang Wang, Jiayan Zhang, Jinyang Liu, Devon McKeon, David Guy Brizan, Giles Blaney, Robert Jacob

[Link](https://programs.sigchi.org/uist/2024/program/content/170939)

Abstract: Brain-Computer Interfaces (BCIs) using functional near-infrared spectroscopy (fNIRS) hold promise for future interactive user interfaces due to their ease of deployment and declining cost. However, they typically require a separate calibration process for each user and task, which can be burdensome. Machine learning helps, but faces a data scarcity problem. Due to inherent inter-user variations in physiological data, it has been typical to create a new annotated training dataset for every new task and user. To reduce dependence on such extensive data collection and labeling, we present an adaptive learning framework, NIRS-X, to harness more easily accessible unlabeled fNIRS data.  NIRS-X includes two key components: NIRSiam and NIRSformer. We use the NIRSiam algorithm to extract generalized brain activity representations from unlabeled fNIRS data obtained from previous users and tasks, and then transfer that knowledge to new users and tasks. In conjunction, we design a neural network, NIRSformer, tailored for capturing both local and global, spatial and temporal relationships in multi-channel fNIRS brain input signals. By using unlabeled data from both a previously released fNIRS2MW visual $n$-back dataset and a newly collected fNIRS2MW audio $n$-back dataset, NIRS-X demonstrates its strong adaptation capability to new users and tasks. Results show comparable or superior performance to supervised methods, making NIRS-X promising for real-world fNIRS-based BCIs.



### Understanding the Effects of Restraining Finger Coactivation in Mid-Air Typing: from a Neuromechanical Perspective
Authors: Hechuan Zhang, Xuewei Liang, Ying Lei, Yanjun Chen, Zhenxuan He, Yu Zhang, Lihan Chen, Hongnan Lin, Teng Han, Feng Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/170941)

Abstract: Typing in mid-air is often perceived as intuitive yet presents challenges due to finger coactivation, a neuromechanical phenomenon that involves involuntary finger movements stemming from the lack of physical constraints. Previous studies were used to examine and address the impacts of finger coactivation using algorithmic approaches. Alternatively, this paper explores the neuromechanical effects of finger coactivation on mid-air typing, aiming to deepen our understanding and provide valuable insights to improve these interactions. We utilized a wearable device that restrains finger coactivation as a prop to conduct two mid-air studies, including a rapid finger-tapping task and a ten-finger typing task. The results revealed that restraining coactivation not only reduced mispresses, which is a classic coactivated error always considered as harm caused by coactivation. Unexpectedly, the reduction of motor control errors and spelling errors, thinking as non-coactivated errors, also be observed.
Additionally, the study evaluated the neural resources involved in motor execution using functional Near Infrared Spectroscopy (fNIRS), which tracked cortical arousal during mid-air typing. The findings demonstrated decreased activation in the primary motor cortex of the left hemisphere when coactivation was restrained, suggesting a diminished motor execution load. This reduction suggests that a portion of neural resources is conserved, which also potentially aligns with perceived lower mental workload and decreased frustration levels.



### What is Affective Touch Made Of? A Soft Capacitive Sensor Array Reveals the Interplay between Shear, Normal Stress and Individuality
Authors: Devyani McLaren, Jian Gao, Xiulun Yin, Rúbia Reis Guerra, Preeti Vyas, Chrys Morton, Xi Laura Cang, Yizhong Chen, Yiyuan Sun, Ying Li, John Madden, Karon MacLean

[Link](https://programs.sigchi.org/uist/2024/program/content/171010)

Abstract: Humans physically express emotion by modulating parameters that register on mammalian skin mechanoreceptors, but are unavailable in current touch-sensing technology. 
Greater sensory richness combined with data on affect-expression composition is a prerequisite to estimating affect from touch, with applications including physical human-robot interaction. To examine shear alongside more easily captured normal stresses, we tailored recent capacitive technology to attain performance suitable for affective touch, creating a flexible, reconfigurable and soft 36-taxel array that detects multitouch normal and 2-dimensional shear at ranges of 1.5kPa-43kPa and $\pm$ 0.3-3.8kPa respectively, wirelessly at ~43Hz (1548 taxels/s). In a deep-learning classification of 9 gestures (N=16), inclusion of shear data improved accuracy to 88\%, compared to 80\% with normal stress data alone, confirming shear stress's expressive centrality. 
Using this rich data, we analyse the interplay of sensed-touch features, gesture attributes and individual differences, propose affective-touch sensing requirements, and share technical considerations for performance and practicality.



### Exploring the Effects of Sensory Conflicts on Cognitive Fatigue in VR Remappings
HONORABLE_MENTION

Authors: Tianren Luo, Gaozhang Chen, Yijian Wen, Pengxiang Wang, yachun fan, Teng Han, Feng Tian

[Link](https://programs.sigchi.org/uist/2024/program/content/171000)

Abstract: Virtual reality (VR) is found to present significant cognitive challenges due to its immersive nature and frequent sensory conflicts. This study systematically investigates the impact of sensory conflicts induced by VR remapping techniques on cognitive fatigue, and unveils their correlation. We utilized three remapping methods (haptic repositioning, head-turning redirection, and giant resizing) to create different types of sensory conflicts, and measured perceptual thresholds to induce various intensities of the conflicts. Through experiments involving cognitive tasks along with subjective and physiological measures, we found that all three remapping methods influenced the onset and severity of cognitive fatigue, with visual-vestibular conflict having the greatest impact. Interestingly, visual-experiential/memory conflict showed a mitigating effect on cognitive fatigue, emphasizing the role of novel sensory experiences. This study contributes to a deeper understanding of cognitive fatigue under sensory conflicts and provides insights for designing VR experiences that align better with human perceptual and cognitive capabilities. 




## Break Q&A: Future Fabrics
### ScrapMap: Interactive Color Layout for Scrap Quilting
Authors: Mackenzie Leake, Ross Daly

[Link](https://programs.sigchi.org/uist/2024/program/content/170743)

Abstract: Scrap quilting is a popular sewing process that involves combining leftover pieces of fabric into traditional patchwork designs. Imagining the possibilities for these leftovers and arranging the fabrics in such a way that achieves visual goals, such as high contrast, can be challenging given the large number of potential fabric assignments within the quilt's design. We formulate the task of designing a scrap quilt as a graph coloring problem with domain-specific coloring and material constraints. Our interactive tool called ScrapMap helps quilters explore these potential designs given their available materials by leveraging the hierarchy of scrap quilt construction (e.g., quilt blocks and motifs) and providing user-directed automatic block coloring suggestions. Our user evaluation indicates that quilters find ScrapMap useful for helping them consider new ways to use their scraps and create visually striking quilts.



### What's in a cable? Abstracting Knitting Design Elements with Blended Raster/Vector Primitives
Authors: Hannah Twigg-Smith, Yuecheng Peng, Emily Whiting, Nadya Peek

[Link](https://programs.sigchi.org/uist/2024/program/content/170811)

Abstract: In chart-based programming environments for machine knitting, patterns are specified at a low level by placing operations on a grid. This highly manual workflow makes it challenging to iterate on design elements such as cables, colorwork, and texture. While vector-based abstractions for knitting design elements may facilitate higher-level manipulation, they often include interdependencies which require stitch-level reconciliation. To address this, we contribute a new way of specifying knits with blended vector and raster primitives. Our abstraction supports the design of interdependent elements like colorwork and texture. We have implemented our blended raster/vector specification in a direct manipulation design tool where primitives are layered and rasterized, allowing for simulation of the resulting knit structure and generation of machine instructions. Through examples, we show how our approach enables higher-level manipulation of various knitting techniques, including intarsia colorwork, short rows, and cables. Specifically, we show how our tool supports the design of complex patterns including origami pleat patterns and capacitive sensor patches.



### Embrogami: Shape-Changing Textiles with Machine Embroidery
Authors: Yu Jiang, Alice Haynes, Narjes Pourjafarian, Jan Borchers, Jürgen Steimle

[Link](https://programs.sigchi.org/uist/2024/program/content/170971)

Abstract: Machine embroidery is a versatile technique for creating custom and entirely fabric-based patterns on thin and conformable textile surfaces. However, existing machine-embroidered surfaces remain static, limiting the interactions they can support. We introduce Embrogami, an approach for fabricating textile structures with versatile shape-changing behaviors. Inspired by origami, we leverage machine embroidery to form finger-tip-scale mountain-and-valley structures on textiles with customized shapes, bistable or elastic behaviors, and modular composition. The structures can be actuated by the user or the system to modify the local textile surface topology, creating interactive elements like toggles and sliders or textile shape displays with an ultra-thin, flexible, and integrated form factor. We provide a dedicated software tool and report results of technical experiments to allow users to flexibly design, fabricate, and deploy customized Embrogami structures. With four application cases, we showcase Embrogami’s potential to create functional and flexible shape-changing textiles with diverse visuo-tactile feedback.



### KODA: Knit-program Optimization by Dependency Analysis
Authors: Megan Hofmann

[Link](https://programs.sigchi.org/uist/2024/program/content/170935)

Abstract: Digital knitting machines have the capability to reliably manufacture seamless, textured, and multi-material garments, but these capabilities are obscured by limiting CAD tools. Recent innovations in computational knitting build on emerging programming infrastructure that gives full access to the machine's capabilities but requires an extensive understanding of machine operations and execution.  In this paper, we contribute a critical missing piece of the knitting-machine programming pipeline--a program optimizer. Program optimization allows programmers to focus on developing novel algorithms that produce desired fabrics while deferring concerns of efficient machine operations to the optimizer. We present KODA, the Knit-program Optimization by Dependency Analysis method. KODA re-orders and reduces machine instructions to reduce knitting time, increase knitting reliability, and manage boilerplate operations that adjust the machine state. The result is a system that enables programmers to write readable and intuitive knitting algorithms while producing efficient and verified programs. 



### X-Hair: 3D Printing Hair-like Structures with Multi-form, Multi-property and Multi-function
Authors: Guanyun Wang, Junzhe Ji, Yunkai Xu, Lei Ren, Xiaoyang Wu, Chunyuan Zheng, Xiaojing Zhou, Xin Tang, Boyu Feng, Lingyun Sun, Ye Tao, Jiaji Li

[Link](https://programs.sigchi.org/uist/2024/program/content/171007)

Abstract: In this paper, we present X-Hair, a method that enables 3D-printed hair with various forms, properties, and functions. We developed a two-step suspend printing strategy to fabricate hair-like structures in different forms (e.g. fluff, bristle, barb) by adjusting parameters including Extrusion Length Ratio and Total Length. Moreover, a design tool is also established for users to customize hair-like structures with various properties (e.g. pointy, stiff, soft) on imported 3D models, which virtually shows the results for previewing and generates G-code files for 3D printing. We demonstrate the design space of X-Hair and evaluate the properties of them with different parameters. Through a series of applications with hair-like structures, we validate X-hair's practical usage of biomimicry, decoration, heat preservation, adhesion, and haptic interaction.



### TouchpadAnyWear: Textile-Integrated Tactile Sensors for Multimodal High Spatial-Resolution Touch Inputs with Motion Artifacts Tolerance
Authors: Junyi Zhao, Pornthep Preechayasomboon, Tyler Christensen, Amirhossein H. Memar, Zhenzhen Shen, Nick Colonnese, Michael Khbeis, Mengjia Zhu

[Link](https://programs.sigchi.org/uist/2024/program/content/170873)

Abstract: This paper presents TouchpadAnyWear, a novel family of textile-integrated force sensors capable of multi-modal touch input, encompassing micro-gesture detection, two-dimensional (2D) continuous input, and force-sensitive strokes. This thin (\textless 1.5~mm) and conformal device features high spatial resolution sensing and motion artifact tolerance through its unique capacitive sensor architecture. The sensor consists of a knitted textile compressive core, sandwiched by stretchable silver electrodes, and conductive textile shielding layers on both sides. With a high-density sensor pixel array (25/cm\textsuperscript{2}), TouchpadAnyWear can detect touch input locations and sizes with millimeter-scale spatial resolution and a wide range of force inputs (0.05~N to 20~N). The incorporation of miniature polymer domes, referred to as ``poly-islands'', onto the knitted textile locally stiffens the sensing areas, thereby reducing motion artifacts during deformation. These poly-islands also provide passive tactile feedback to users, allowing for eyes-free localization of the active sensing pixels. Design choices and sensor performance are evaluated using in-depth mechanical characterization. Demonstrations include an 8-by-8 grid sensor as a miniature high-resolution touchpad and a T-shaped sensor for thumb-to-finger micro-gesture input. User evaluations validate the effectiveness and usability of TouchpadAnyWear in daily interaction contexts, such as tapping, forceful pressing, swiping, 2D cursor control, and 2D stroke-based gestures. This paper further discusses potential applications and explorations for TouchpadAnyWear in wearable smart devices, gaming, and augmented reality devices.




## Break Q&A: Dynamic Objects & Materials
### MagneDot: Integrated Fabrication and Actuation Methods of Dot-Based Magnetic Shape Displays
Authors: Lingyun Sun, Yitao Fan, Boyu Feng, Yifu Zhang, Deying Pan, Yiwen Ren, Yuyang Zhang, Qi Wang, Ye Tao, Guanyun Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170860)

Abstract: This paper presents MagneDot, a novel method for making interactive magnetic shape displays through an integrated fabrication process. Magnetic soft materials can potentially create fast, responsive morphing structures for interactions. However, novice users and designers typically do not have access to sophisticated equipment and materials or cannot afford heavy labor to create interactive objects based on this material. Modified from an open-source 3D printer, the fabrication system of MagneDot integrates the processes of mold-making, pneumatic extrusion, magnetization, and actuation, using cost-effective materials only. By providing a design tool, MagneDot allows users to generate G-codes for fabricating and actuating displays of various morphing effects. Finally, a series of design examples demonstrate the possibilities of shape displays enabled by MagneDot.



### CARDinality: Interactive Card-shaped Robots with Locomotion and Haptics using Vibration
Authors: Aditya Retnanto, Emilie Faracci, Anup Sathya, Yu-Kai Hung, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170995)

Abstract: This paper introduces a novel approach to interactive robots by leveraging the form-factor of cards to create thin robots equipped with vibrational capabilities for locomotion and haptic feedback. The system is composed of flat-shaped robots with on-device sensing and wireless control, which offer lightweight portability and scalability. This research introduces a hardware prototype to explore the possibility of ‘vibration-based omni-directional sliding locomotion’. Applications include augmented card playing, educational tools, and assistive technology, which showcase CARDinality’s versatility in tangible interaction.




### PortaChrome: A Portable Contact Light Source for Integrated Re-Programmable Multi-Color Textures
Authors: Yunyi Zhu, Cedric Honnet, Yixiao Kang, Junyi Zhu, Angelina Zheng, Kyle Heinz, Grace Tang, Luca Musk, Michael Wessely, Stefanie Mueller

[Link](https://programs.sigchi.org/uist/2024/program/content/170742)

Abstract: In this paper, we present PortaChrome, a portable light source that can be attached to everyday objects to reprogram the color and texture of surfaces that come in contact with them. When PortaChrome makes contact with objects previously coated with photochromic dye, the UV and RGB LEDs inside PortaChrome create multi-color textures on the objects. In contrast to prior work, which used projectors for the color-change, PortaChrome has a thin and flexible form factor, which allows the color-change process to be integrated into everyday user interaction. Because of the close distance between the light source and the photochromic object, PortaChrome creates color textures in less than 4 minutes on average, which is 8 times faster than prior work. We demonstrate PortaChrome with four application examples, including data visualizations on textiles and dynamic designs on wearables. 



### Augmented Object Intelligence with XR-Objects
Authors: Mustafa Doga Dogan, Eric Gonzalez, Karan Ahuja, Ruofei Du, Andrea Colaço, Johnny Lee, Mar Gonzalez-Franco, David Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170733)

Abstract: Seamless integration of physical objects as interactive digital entities remains a challenge for spatial computing. This paper explores Augmented Object Intelligence (AOI) in the context of XR, an interaction paradigm that aims to blur the lines between digital and physical by equipping real-world objects with the ability to interact as if they were digital, where every object has the potential to serve as a portal to digital functionalities. Our approach utilizes real-time object segmentation and classification, combined with the power of Multimodal Large Language Models (MLLMs), to facilitate these interactions without the need for object pre-registration. We implement the AOI concept in the form of XR-Objects, an open-source prototype system that provides a platform for users to engage with their physical environment in contextually relevant ways using object-based context menus. This system enables analog objects to not only convey information but also to initiate digital actions, such as querying for details or executing tasks. Our contributions are threefold: (1) we define the AOI concept and detail its advantages over traditional AI assistants, (2) detail the XR-Objects system’s open-source design and implementation, and (3) show its versatility through various use cases and a user study.




## Break Q&A: Prototyping
### ProtoDreamer: A Mixed-prototype Tool Combining Physical Model and Generative AI to Support Conceptual Design
Authors: Hongbo ZHANG, Pei Chen, Xuelong Xie, Chaoyi Lin, Lianyan Liu, Zhuoshu Li, Weitao You, Lingyun Sun

[Link](https://programs.sigchi.org/uist/2024/program/content/170974)

Abstract: Prototyping serves as a critical phase in the industrial conceptual design process, enabling exploration of problem space and identification of solutions. Recent advancements in large-scale generative models have enabled AI to become a co-creator in this process. However, designers often consider generative AI challenging due to the necessity to follow computer-centered interaction rules, diverging from their familiar design materials and languages. Physical prototype is a commonly used design method, offering unique benefits in prototype process, such as intuitive understanding and tangible testing. In this study, we propose ProtoDreamer, a mixed-prototype tool that synergizes generative AI with physical prototype to support conceptual design. ProtoDreamer allows designers to construct preliminary prototypes using physical materials, while AI recognizes these forms and vocal inputs to generate diverse design alternatives. This tool empowers designers to tangibly interact with prototypes, intuitively convey design intentions to AI, and continuously draw inspiration from the generated artifacts. An evaluation study confirms ProtoDreamer’s utility and strengths in time efficiency, creativity support, defects exposure, and detailed thinking facilitation.



### TorqueCapsules: Fully-Encapsulated Flywheel Actuation Modules for Designing and Prototyping Movement-Based and Kinesthetic Interaction
Authors: Willa Yunqi Yang, Yifan Zou, Jingle Huang, Raouf Abujaber, Ken Nakagaki

[Link](https://programs.sigchi.org/uist/2024/program/content/170857)

Abstract: Flywheels are unique, versatile actuators that store and convert kinetic energy to torque, widely utilized in aerospace, robotics, haptics, and more. However, prototyping interaction using flywheels is not trivial due to safety concerns, unintuitive operation, and implementation challenges. 
We present TorqueCapsules: self-contained, fully-encapsulated flywheel actuation modules that make the flywheel actuators easy to control, safe to interact with, and quick to reconfigure and customize. By fully encapsulating the actuators with a wireless microcontroller, a battery, and other components, the module can be readily attached, embedded, or stuck to everyday objects, worn to people’s bodies, or combined with other devices. With our custom GUI, both novices and expert users can easily control multiple modules to design and prototype movements and kinesthetic haptics unique to flywheel actuation. We demonstrate various applications, including actuated everyday objects, wearable haptics, and expressive robots. We conducted workshops for novices and experts to employ TorqueCapsules to collect qualitative feedback and further application examples.



### AniCraft: Crafting Everyday Objects as Physical Proxies for Prototyping 3D Character Animation in Mixed Reality
Authors: Boyu Li, Linping Yuan, Zhe Yan, Qianxi Liu, Yulin Shen, Zeyu Wang

[Link](https://programs.sigchi.org/uist/2024/program/content/170881)

Abstract: We introduce AniCraft, a mixed reality system for prototyping 3D character animation using physical proxies crafted from everyday objects. Unlike existing methods that require specialized equipment to support the use of physical proxies, AniCraft only requires affordable markers, webcams, and daily accessible objects and materials. AniCraft allows creators to prototype character animations through three key stages: selection of virtual characters, fabrication of physical proxies, and manipulation of these proxies to animate the characters. This authoring workflow is underpinned by diverse physical proxies, manipulation types, and mapping strategies, which ease the process of posing virtual characters and mapping user interactions with physical proxies to animated movements of virtual characters. We provide a range of cases and potential applications to demonstrate how diverse physical proxies can inspire user creativity. User experiments show that our system can outperform traditional animation methods for rapid prototyping. Furthermore, we provide insights into the benefits and usage patterns of different materials, which lead to design implications for future research.



### Mul-O: Encouraging Olfactory Innovation in Various Scenarios Through a Task-Oriented Development Platform
Authors: Peizhong Gao, Fan Liu, Di Wen, Yuze Gao, Linxin Zhang, Chikelei Wang, Qiwei Zhang, Yu Zhang, Shao-en Ma, Qi Lu, Haipeng Mi, YINGQING XU

[Link](https://programs.sigchi.org/uist/2024/program/content/170886)

Abstract: Olfactory interfaces are pivotal in HCI, yet their development is hindered by limited application scenarios, stifling the discovery of new research opportunities. This challenge primarily stems from existing design tools focusing predominantly on odor display devices and the creation of standalone olfactory experiences, rather than enabling rapid adaptation to various contexts and tasks. Addressing this, we introduce Mul-O, a novel task-oriented development platform crafted to aid semi-professionals in navigating the diverse requirements of potential application scenarios and effectively prototyping ideas.
Mul-O facilitates the swift association and integration of olfactory experiences into functional designs, system integrations, and concept validations. Comprising a web UI for task-oriented development, an API server for seamless third-party integration, and wireless olfactory display hardware, Mul-O significantly enhances the ideation and prototyping process in multisensory tasks. This was verified by a 15-day workshop attended by 30 participants. The workshop produced seven innovative projects, underscoring Mul-O's efficacy in fostering olfactory innovation.




## Break Q&A: New Vizualizations
### VisCourt: In-Situ Guidance for Interactive Tactic Training in Mixed Reality
Authors: Liqi Cheng, Hanze Jia, Lingyun Yu, Yihong Wu, Shuainan Ye, Dazhen Deng, Hui Zhang, Xiao Xie, Yingcai Wu

[Link](https://programs.sigchi.org/uist/2024/program/content/170791)

Abstract: In team sports like basketball, understanding and executing tactics---coordinated plans of movements among players---are crucial yet complex, requiring extensive practice. These tactics require players to develop a keen sense of spatial and situational awareness. Traditional coaching methods, which mainly rely on basketball tactic boards and video instruction, often fail to bridge the gap between theoretical learning and the real-world application of tactics, due to shifts in view perspectives and a lack of direct experience with tactical scenarios. To address this challenge, we introduce VisCourt, a Mixed Reality (MR) tactic training system, in collaboration with a professional basketball team. To set up the MR training environment, we employed semi-automatic methods to simulate realistic 3D tactical scenarios and iteratively designed visual in-situ guidance. This approach enables full-body engagement in interactive training sessions on an actual basketball court and provides immediate feedback, significantly enhancing the learning experience. A user study with athletes and enthusiasts shows the effectiveness and satisfaction with VisCourt in basketball training and offers insights for the design of future SportsXR training systems.



### Block and Detail: Scaffolding Sketch-to-Image Generation
Authors: Vishnu Sarukkai, Lu Yuan, Mia Tang, Maneesh Agrawala, Kayvon Fatahalian

[Link](https://programs.sigchi.org/uist/2024/program/content/170911)

Abstract: We introduce a novel sketch-to-image tool that aligns with the iterative refinement process of artists. Our tool lets users sketch blocking strokes to coarsely represent the placement and form of objects and detail strokes to refine their shape and silhouettes. We develop a two-pass algorithm for generating high-fidelity images from such sketches at any point in the iterative process. In the first pass we use a ControlNet to generate an image that strictly follows all the strokes (blocking and detail) and in the second pass we add variation by renoising regions surrounding blocking strokes. We also present a dataset generation scheme that, when used to train a ControlNet architecture, allows regions that do not contain strokes to be interpreted as not-yet-specified regions rather than empty space. We show that this partial-sketch-aware ControlNet can generate coherent elements from partial sketches that only contain a small number of strokes. The high-fidelity images produced by our approach serve as scaffolds that can help the user adjust the shape and proportions of objects or add additional elements to the composition. We demonstrate the effectiveness of our approach with a variety of examples and evaluative comparisons. Quantitatively, novice viewers prefer the quality of images from our algorithm over a baseline Scribble ControlNet for 82% of the pairs and found our images had less distortion in 80% of the pairs.



### EVE: Enabling Anyone to Train Robots using Augmented Reality
Authors: Jun Wang, Chun-Cheng Chang, Jiafei Duan, Dieter Fox, Ranjay Krishna

[Link](https://programs.sigchi.org/uist/2024/program/content/170803)

Abstract: The increasing affordability of robot hardware is accelerating the integration of robots into everyday activities. However, training a robot to automate a task requires expensive trajectory data where a trained human annotator moves a physical robot to train it. Consequently, only those with access to robots produce demonstrations to train robots. In this work, we remove this restriction with EVE, an iOS app that enables everyday users to train robots using intuitive augmented reality visualizations, without needing a physical robot. With EVE, users can collect demonstrations by specifying waypoints with their hands, visually inspecting the environment for obstacles, modifying existing waypoints, and verifying collected trajectories. In a user study (N=14, D=30) consisting of three common tabletop tasks, EVE outperformed three state-of-the-art interfaces in success rate and was comparable to kinesthetic teaching—physically moving a physical robot—in completion time, usability, motion intent communication, enjoyment, and preference (mean of p=0.30). EVE allows users to train robots for personalized tasks, such as sorting desk supplies, organizing ingredients, or setting up board games. We conclude by enumerating limitations and design considerations for future AR-based demonstration collection systems for robotics.



### avaTTAR: Table Tennis Stroke Training with On-body and Detached Visualization in Augmented Reality
Authors: Dizhi Ma, Xiyun Hu, Jingyu Shi, Mayank Patel, Rahul Jain, Ziyi Liu, Zhengzhe Zhu, Karthik Ramani

[Link](https://programs.sigchi.org/uist/2024/program/content/170894)

Abstract: Table tennis stroke training is a critical aspect of player development. We designed a new augmented reality (AR) system, avaTTAR, for table tennis stroke training. The system provides both “on-body” (first-person view) and “detached” (third-person view)
visual cues, enabling users to visualize target strokes and correct their attempts effectively with this dual perspectives setup. By employing a combination of pose estimation algorithms and IMU sensors, avaTTAR captures and reconstructs the 3D body pose and paddle orientation of users during practice, allowing real-time comparison with expert strokes. Through a user study, we affirm avaTTAR ’s capacity to amplify player experience and training results




## Break Q&A: Movement-based UIs
### Feminist Interaction Techniques: Social Consent Signals to Deter NCIM Screenshots
Authors: Li Qiwei, Francesca Lameiro, Shefali Patel, Cristi Isaula-Reyes, Eytan Adar, Eric Gilbert, Sarita Schoenebeck

[Link](https://programs.sigchi.org/uist/2024/program/content/170858)

Abstract: Non-consensual Intimate Media (NCIM) refers to the distribution of sexual or intimate content without consent. NCIM is common and causes significant emotional, financial, and reputational harm. We developed Hands-Off, an interaction technique for messaging applications that deters non-consensual screenshots. Hands-Off requires recipients to perform a hand gesture in the air, above the device, to unlock media—which makes simultaneous screenshotting difficult. A lab study shows that Hands-Off gestures are easy
to perform and reduce non-consensual screenshots by 67%. We conclude by generalizing this approach and introduce the idea of Feminist Interaction Techniques (FIT), interaction techniques that encode feminist values and speak to societal problems, and reflect on FIT’s opportunities and limitations.



### Effects of Computer Mouse Lift-off Distance Settings in Mouse Lifting Action
Authors: Munjeong Kim, Sunjun Kim

[Link](https://programs.sigchi.org/uist/2024/program/content/170957)

Abstract: This study investigates the effect of Lift-off Distance (LoD) on a computer mouse, which refers to the height at which a mouse sensor stops tracking when lifted off the surface. Although a low LoD is generally preferred to avoid unintentional cursor movement in mouse lifting (=clutching), especially in first-person shooter games, it may reduce tracking stability. 
We conducted a psychophysical experiment to measure the perceptible differences between LoD levels and quantitatively measured the unintentional cursor movement error and tracking stability at four levels of LoD while users performed mouse lifting. The results showed a trade-off between movement error and tracking stability at varying levels of LoD. Our findings offer valuable information on optimal LoD settings, which could serve as a guide for choosing a proper mouse device for enthusiastic gamers. 



### DisMouse: Disentangling Information from Mouse Movement Data
Authors: Guanhua Zhang, Zhiming Hu, Andreas Bulling

[Link](https://programs.sigchi.org/uist/2024/program/content/170847)

Abstract: Mouse movement data contain rich information about users, performed tasks, and user interfaces, but separating the respective components remains challenging and unexplored. As a first step to address this challenge, we propose DisMouse – the first method to disentangle user-specific and user-independent information and stochastic variations from mouse movement data. At the core of our method is an autoencoder trained in a semi-supervised fashion, consisting of a self-supervised denoising diffusion process and a supervised contrastive user identification module. Through evaluations on three datasets, we show that DisMouse 1) captures complementary information of mouse input, hence providing an interpretable framework for modelling mouse movements, 2) can be used to produce refined features, thus enabling various applications such as personalised and variable mouse data generation, and 3) generalises across different datasets. Taken together, our results underline the significant potential of disentangled representation learning for explainable, controllable, and generalised mouse behaviour modelling.



### Wheeler: A Three-Wheeled Input Device for Usable, Efficient, and Versatile Non-Visual Interaction
HONORABLE_MENTION

Authors: Md Touhidul Islam, Noushad Sojib, Imran Kabir, Ashiqur Rahman Amit, Mohammad Ruhul Amin, Syed Masum Billah

[Link](https://programs.sigchi.org/uist/2024/program/content/170848)

Abstract: Blind users rely on keyboards and assistive technologies like screen readers to interact with user interface (UI) elements. In modern applications with complex UI hierarchies, navigating to different UI elements poses a significant accessibility challenge. Users must listen to screen reader audio descriptions and press relevant keyboard keys one at a time. This paper introduces Wheeler, a novel three-wheeled, mouse-shaped stationary input device, to address this issue. Informed by participatory sessions, Wheeler enables blind users to navigate up to three hierarchical levels in an app independently using three wheels instead of navigating just one level at a time using a keyboard. The three wheels also offer versatility, allowing users to repurpose them for other tasks, such as 2D cursor manipulation. A study with 12 blind users indicates a significant reduction (40%) in navigation time compared to using a keyboard. Further, a diary study with our blind co-author highlights Wheeler's additional benefits, such as accessing UI elements with partial metadata and facilitating mixed-ability collaboration.




## Break Q&A: Sound & Music
### SonoHaptics: An Audio-Haptic Cursor for Gaze-Based Object Selection in XR
Authors: Hyunsung Cho, Naveen Sendhilnathan, Michael Nebeling, Tianyi Wang, Purnima Padmanabhan, Jonathan Browder, David Lindlbauer, Tanya Jonker, Kashyap Todi

[Link](https://programs.sigchi.org/uist/2024/program/content/170927)

Abstract: We introduce SonoHaptics, an audio-haptic cursor for gaze-based 3D object selection. SonoHaptics addresses challenges around providing accurate visual feedback during gaze-based selection in Extended Reality (XR), e.g., lack of world-locked displays in no- or limited-display smart glasses and visual inconsistencies. To enable users to distinguish objects without visual feedback, SonoHaptics employs the concept of cross-modal correspondence in human perception to map visual features of objects (color, size, position, material) to audio-haptic properties (pitch, amplitude, direction, timbre). We contribute data-driven models for determining cross-modal mappings of visual features to audio and haptic features, and a computational approach to automatically generate audio-haptic feedback for objects in the user's environment. SonoHaptics provides global feedback that is unique to each object in the scene, and local feedback to amplify differences between nearby objects. Our comparative evaluation shows that SonoHaptics enables accurate object identification and selection in a cluttered scene without visual feedback.



### SonifyAR: Context-Aware Sound Generation in Augmented Reality
Authors: Xia Su, Jon Froehlich, Eunyee Koh, Chang Xiao

[Link](https://programs.sigchi.org/uist/2024/program/content/170866)

Abstract: Sound plays a crucial role in enhancing user experience and immersiveness in Augmented Reality (AR). However, current platforms lack support for AR sound authoring due to limited interaction types, challenges in collecting and specifying context information, and difficulty in acquiring matching sound assets. We present SonifyAR, an LLM-based AR sound authoring system that generates context-aware sound effects for AR experiences. SonifyAR expands the current design space of AR sound and implements a Programming by Demonstration (PbD) pipeline to automatically collect contextual information of AR events, including virtual-content-semantics and real-world context. This context information is then processed by a large language model to acquire sound effects with Recommendation, Retrieval, Generation, and Transfer methods. To evaluate the usability and performance of our system, we conducted a user study with eight participants and created five example applications, including an AR-based science experiment, and an assistive application for low-vision AR users.



### Auptimize: Optimal Placement of Spatial Audio Cues for Extended Reality
Authors: Hyunsung Cho, Alexander Wang, Divya Kartik, Emily Xie, Yukang Yan, David Lindlbauer

[Link](https://programs.sigchi.org/uist/2024/program/content/170952)

Abstract: Spatial audio in Extended Reality (XR) provides users with better awareness of where virtual elements are placed, and efficiently guides them to events such as notifications, system alerts from different windows, or approaching avatars. Humans, however, are inaccurate in localizing sound cues, especially with multiple sources due to limitations in human auditory perception such as angular discrimination error and front-back confusion. This decreases the efficiency of XR interfaces because users misidentify from which XR element a sound is coming. To address this, we propose Auptimize, a novel computational approach for placing XR sound sources, which mitigates such localization errors by utilizing the ventriloquist effect. Auptimize disentangles the sound source locations from the visual elements and relocates the sound sources to optimal positions for unambiguous identification of sound cues, avoiding errors due to inter-source proximity and front-back confusion. Our evaluation shows that Auptimize decreases spatial audio-based source identification errors compared to playing sound cues at the paired visual-sound locations. We demonstrate the applicability of Auptimize for diverse spatial audio-based interactive XR scenarios.



### EarHover: Mid-Air Gesture Recognition for Hearables Using Sound Leakage Signals
BEST_PAPER

Authors: Shunta Suzuki, Takashi Amesaka, Hiroki Watanabe, Buntarou Shizuki, Yuta Sugiura

[Link](https://programs.sigchi.org/uist/2024/program/content/170787)

Abstract: We introduce EarHover, an innovative system that enables mid-air gesture input for hearables. Mid-air gesture input, which eliminates the need to touch the device and thus helps to keep hands and the device clean, has been known to have high demand based on previous surveys. However, existing mid-air gesture input methods for hearables have been limited to adding cameras or infrared sensors. By focusing on the sound leakage phenomenon unique to hearables, we have realized mid-air gesture recognition using a speaker and an external microphone that are highly compatible with hearables. The signal leaked to the outside of the device due to sound leakage can be measured by an external microphone, which detects the differences in reflection characteristics caused by the hand's speed and shape during mid-air gestures.
Among 27 types of gestures, we determined the seven most suitable gestures for EarHover in terms of signal discrimination and user acceptability. We then evaluated the gesture detection and classification performance of two prototype devices (in-ear type/open-ear type) for real-world application scenarios.



### Towards Music-Aware Virtual Assistants
Authors: Alexander Wang, David Lindlbauer, Chris Donahue

[Link](https://programs.sigchi.org/uist/2024/program/content/170955)

Abstract: We propose a system for modifying spoken notifications in a manner that is sensitive to the music a user is listening to. Spoken notifications provide convenient access to rich information without the need for a screen. Virtual assistants see prevalent use in hands-free settings such as driving or exercising, activities where users also regularly enjoy listening to music. In such settings, virtual assistants will temporarily mute a user's music to improve intelligibility. However, users may perceive these interruptions as intrusive, negatively impacting their music-listening experience. To address this challenge, we propose the concept of music-aware virtual assistants, where speech notifications are modified to resemble a voice singing in harmony with the user's music. We contribute a system that processes user music and notification text to produce a blended mix, replacing original song lyrics with the notification content. In a user study comparing musical assistants to standard virtual assistants, participants expressed that musical assistants fit better with music, reduced intrusiveness, and provided a more delightful listening experience overall.




