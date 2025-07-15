import { useEffect, useState } from "react";
import axios from "axios";

function Journal({ token }) {
  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchJournal = async () => {
      try {
        const res = await axios.get("http://localhost:8000/journal", {
          headers: { Authorization: `Bearer ${token}` }
        });
        setContent(res.data.content || "");
      } catch (err) {
        console.error("Failed to load journal", err);
      }
    };
    fetchJournal();
  }, [token]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/journal", { content }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setMessage("Journal saved.");
      setTimeout(() => setMessage(""), 3000);
    } catch (err) {
      console.error("Failed to save journal", err);
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Daily Journal</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Write your thoughts..."
          className="w-full h-64 border p-2 rounded"
        />
        {message && <p className="text-green-500">{message}</p>}
        <button type="submit" className="bg-purple-600 text-white px-4 py-2 rounded">Save Journal</button>
      </form>
    </div>
  );
}

export default Journal;
