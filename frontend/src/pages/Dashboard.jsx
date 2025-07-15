import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard({ token }) {
  const [entries, setEntries] = useState([]);
  const [form, setForm] = useState({
    title: "",
    content: "",
    type: "idea",
    tags: "",
    source: "",
    status: "inbox"
  });

  const fetchEntries = async () => {
    try {
      const res = await axios.get("http://localhost:8000/entries", {
        headers: { Authorization: `Bearer ${token}` }
      });
      setEntries(res.data);
    } catch (err) {
      console.error("Failed to fetch entries", err);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/entries", form, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setForm({
        title: "",
        content: "",
        type: "idea",
        tags: "",
        source: "",
        status: "inbox"
      });
      fetchEntries();
    } catch (err) {
      console.error("Failed to submit entry", err);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Create Entry</h2>
      <form onSubmit={handleSubmit} className="space-y-4 mb-6">
        <input name="title" value={form.title} onChange={handleChange} placeholder="Title" required className="w-full border p-2 rounded" />
        <textarea name="content" value={form.content} onChange={handleChange} placeholder="Content" className="w-full border p-2 rounded" />
        <input name="tags" value={form.tags} onChange={handleChange} placeholder="Tags (comma separated)" className="w-full border p-2 rounded" />
        <select name="type" value={form.type} onChange={handleChange} className="w-full border p-2 rounded">
          <option value="idea">Idea</option>
          <option value="link">Link</option>
          <option value="task">Task</option>
          <option value="file">File</option>
        </select>
        <input name="source" value={form.source} onChange={handleChange} placeholder="Source" className="w-full border p-2 rounded" />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Save</button>
      </form>

      <h3 className="text-xl font-semibold mb-2">Your Entries</h3>
      {entries.length === 0 && <p>No entries yet.</p>}
      <ul className="space-y-2">
        {entries.map((entry) => (
          <li key={entry.id} className="border p-2 rounded shadow-sm">
            <strong>{entry.title}</strong> <em className="text-sm text-gray-500">({entry.type})</em>
            <p>{entry.content}</p>
            {entry.tags && <p className="text-sm text-gray-600">Tags: {entry.tags}</p>}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
