// Extract Blog ID from URL
const urlParams = new URLSearchParams(window.location.search);
const blogId = urlParams.get("id");

// Find Blog by ID
const blog = blogs.find((b) => b.id == blogId);

// Render Blog Details
const renderBlogDetails = () => {
  const blogDetails = document.getElementById("blog-details");
  if (!blog) {
    blogDetails.innerHTML = "<p>Blog not found!</p>";
    return;
  }

  blogDetails.innerHTML = `
    <h1>${blog.title}</h1>
    <img src="${blog.image}" alt="${blog.title}">
    <p><strong>Author:</strong> ${blog.author}</p>
    <p><strong>Date:</strong> ${blog.date}</p>
    <p><strong>Category:</strong> ${blog.category}</p>
    <p>${blog.content}</p>
  `;
};

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

// Initial Render
renderBlogDetails();
