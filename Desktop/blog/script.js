// Blog Data
const blogs = [
  {
    id: 1,
    title: "Hope dies last",
    category: "Art",
    date: "16 March 2022",
    author: "Jakob Grönberg",
    duration: "14m",
    image: "images/blog1.jpg",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    content: "Full content of Hope dies last...",
  },
  {
    id: 2,
    title: "Don’t close your eyes",
    category: "Art",
    date: "16 March 2022",
    author: "Jakob Grönberg",
    duration: "14m",
    image: "images/blog2.jpg",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    content: "Full content of Don’t close your eyes...",
  },
  {
    id: 3,
    title: "The best art museums",
    category: "Sculptures",
    date: "16 March 2022",
    author: "Jakob Grönberg",
    duration: "14m",
    image: "images/blog3.jpg",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    content: "Full content of The best art museums...",
  },
  {
    id: 4,
    title: "Street art festival",
    category: "Street Art",
    date: "16 March 2022",
    author: "Jakob Grönberg",
    duration: "14m",
    image: "images/blog4.jpg",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
    content: "Full content of Street art festival...",
  },
];

// Render Blogs
const renderBlogs = (blogsToRender) => {
  const blogList = document.getElementById("blog-list");
  blogList.innerHTML = "";

  blogsToRender.forEach((blog) => {
    const blogCard = document.createElement("div");
    blogCard.className = "blog-card";
    blogCard.innerHTML = `
      <img src="${blog.image}" alt="${blog.title}">
      <div class="content">
        <h2>${blog.title}</h2>
        <p>Category: ${blog.category}</p>
        <p>${blog.duration} read</p>
        <p>${blog.description}</p>
        <a class="read-more" href="details.html?id=${blog.id}">Read More</a>
      </div>
    `;
    blogList.appendChild(blogCard);
  });
};

// Filter Blogs by Category
document.querySelectorAll("nav a").forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const category = e.target.getAttribute("href").substring(1);
    const filteredBlogs = category === "all" ? blogs : blogs.filter((blog) => blog.category.toLowerCase() === category);
    renderBlogs(filteredBlogs);
  });
});

// Search Blogs
document.getElementById("search-input").addEventListener("input", (e) => {
  const query = e.target.value.toLowerCase();
  const filteredBlogs = blogs.filter(
    (blog) => blog.title.toLowerCase().includes(query) || blog.description.toLowerCase().includes(query)
  );
  renderBlogs(filteredBlogs);
});

// Initial Render
renderBlogs(blogs);

// Comment Section Functionality
const commentSection = document.createElement('div');
commentSection.className = 'comment-section';
commentSection.innerHTML = `
  <h3>Comments</h3>
  <input type="text" id="name" placeholder="Your Name">
  <textarea id="comment" placeholder="Your Comment"></textarea>
  <button id="submit-comment">Submit</button>
  <div id="comments-list"></div>
`;
document.getElementById("blog-list").appendChild(commentSection);

// Handle Comment Submission
document.getElementById("submit-comment").addEventListener("click", () => {
  const name = document.getElementById("name").value;
  const comment = document.getElementById("comment").value;
  if (name && comment) {
    const commentsList = document.getElementById("comments-list");
    const newComment = document.createElement("p");
    newComment.innerHTML = `<strong>${name}:</strong> ${comment}`;
    commentsList.appendChild(newComment);
    document.getElementById("name").value = '';
    document.getElementById("comment").value = '';
  }
});
